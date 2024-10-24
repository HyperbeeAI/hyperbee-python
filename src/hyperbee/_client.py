# File adapted from the 

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources
from openai import _exceptions
from openai._qs import Querystring
from openai._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from openai._utils import (
    is_given,
    is_mapping,
    get_async_library,
)
from ._version import __version__
from openai._streaming import Stream as Stream, AsyncStream as AsyncStream
from openai._exceptions import OpenAIError as HyperBeeError, APIStatusError
from openai._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "HyperBee",
    "AsyncHyperBee",
    "Client",
    "AsyncClient",
]


class HyperBee(SyncAPIClient):
    completions: resources.Completions
    chat: resources.Chat
    models: resources.Models
    with_raw_response: HyperBeeWithRawResponse
    with_streaming_response: HyperBeeWithStreamedResponse

    # client options
    api_key: str
    organization: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        organization: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous openai client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `HYPERBEE_API_KEY`
        - `organization` from `HYPERBEE_ORG_ID`
        """
        if api_key is None:
            api_key = os.environ.get("HYPERBEE_API_KEY")
        if api_key is None:
            raise HyperBeeError(
                "The api_key client option must be set either by passing api_key to the client or by setting the HYPERBEE_API_KEY environment variable"
            )
        self.api_key = api_key

        if organization is None:
            organization = os.environ.get("HYPERBEE_ORG_ID")
        self.organization = organization

        if base_url is None:
            base_url = os.environ.get("HYPERBEE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.hyperbee.ai/v1/"

        self._chat_base_url = "https://api.hyperbee.ai/v1/"
        self._rag_base_url = "https://api-rag.hyperbee.ai/v1/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = Stream

        self.completions = resources.Completions(self)
        self.chat = resources.Chat(self)
        self.models = resources.Models(self)
        self.with_raw_response = HyperBeeWithRawResponse(self)
        self.with_streaming_response = HyperBeeWithStreamedResponse(self)
        self.pipeline = resources.Pipeline(self)
        self.batch_request = resources.batch_request(self)

    def set_base_url_for_request(self, namespace: str | None = None):
        new_base_url = self._rag_base_url if namespace not in (None, NOT_GIVEN) else self._chat_base_url

        if new_base_url != self.base_url:
            # Reinitialize the client with the new base URL
            self.__init__(
                api_key=self.api_key,
                organization=self.organization,
                base_url=new_base_url,
                timeout=self.timeout,
                max_retries=self.max_retries,
                default_headers=self._custom_headers,
                default_query=self._custom_query,
                http_client=self._client,
                _strict_response_validation=self._strict_response_validation,
            )

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "HyperBee-Organization": self.organization if self.organization is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        organization: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            organization=organization or self.organization,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        data = body.get("error", body) if is_mapping(body) else body
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=data)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=data)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=data)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=data)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=data)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=data)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=data)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=data)
        return APIStatusError(err_msg, response=response, body=data)


class AsyncHyperBee(AsyncAPIClient):
    completions: resources.AsyncCompletions
    chat: resources.AsyncChat
    models: resources.AsyncModels
    with_raw_response: AsyncHyperBeeWithRawResponse
    with_streaming_response: AsyncHyperBeeWithStreamedResponse

    # client options
    api_key: str
    organization: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        organization: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async openai client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `HYPERBEE_API_KEY`
        - `organization` from `HYPERBEE_ORG_ID`
        """
        if api_key is None:
            api_key = os.environ.get("HYPERBEE_API_KEY")
        if api_key is None:
            raise HyperBeeError(
                "The api_key client option must be set either by passing api_key to the client or by setting the HYPERBEE_API_KEY environment variable"
            )
        self.api_key = api_key

        if organization is None:
            organization = os.environ.get("HYPERBEE_ORG_ID")
        self.organization = organization

        if base_url is None:
            base_url = os.environ.get("HYPERBEE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.hyperbee.ai/v1/"

        self._chat_base_url = "https://api.hyperbee.ai/v1/"
        self._rag_base_url = "https://not-api-rag.hyperbee.ai/v1/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = AsyncStream

        self.completions = resources.AsyncCompletions(self)
        self.chat = resources.AsyncChat(self)
        self.models = resources.AsyncModels(self)
        self.with_raw_response = AsyncHyperBeeWithRawResponse(self)
        self.with_streaming_response = AsyncHyperBeeWithStreamedResponse(self)
        self.pipeline = resources.AsyncPipeline(self)

    def set_base_url_for_request(self, namespace: str | None = None):
        new_base_url = self._rag_base_url if namespace not in (None, NOT_GIVEN) else self._chat_base_url

        if new_base_url != self.base_url:
            # Reinitialize the client with the new base URL
            self.__init__(
                api_key=self.api_key,
                organization=self.organization,
                base_url=new_base_url,
                timeout=self.timeout,
                max_retries=self.max_retries,
                default_headers=self._custom_headers,
                default_query=self._custom_query,
                http_client=self._client,
                _strict_response_validation=self._strict_response_validation,
            )

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "HyperBee-Organization": self.organization if self.organization is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        organization: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            organization=organization or self.organization,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        data = body.get("error", body) if is_mapping(body) else body
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=data)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=data)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=data)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=data)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=data)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=data)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=data)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=data)
        return APIStatusError(err_msg, response=response, body=data)


class HyperBeeWithRawResponse:
    def __init__(self, client: HyperBee) -> None:
        self.completions = resources.CompletionsWithRawResponse(client.completions)
        self.chat = resources.ChatWithRawResponse(client.chat)
        self.models = resources.ModelsWithRawResponse(client.models)


class AsyncHyperBeeWithRawResponse:
    def __init__(self, client: AsyncHyperBee) -> None:
        self.completions = resources.AsyncCompletionsWithRawResponse(client.completions)
        self.chat = resources.AsyncChatWithRawResponse(client.chat)
        self.models = resources.AsyncModelsWithRawResponse(client.models)


class HyperBeeWithStreamedResponse:
    def __init__(self, client: HyperBee) -> None:
        self.completions = resources.CompletionsWithStreamingResponse(client.completions)
        self.chat = resources.ChatWithStreamingResponse(client.chat)
        self.models = resources.ModelsWithStreamingResponse(client.models)


class AsyncHyperBeeWithStreamedResponse:
    def __init__(self, client: AsyncHyperBee) -> None:
        self.completions = resources.AsyncCompletionsWithStreamingResponse(client.completions)
        self.chat = resources.AsyncChatWithStreamingResponse(client.chat)
        self.models = resources.AsyncModelsWithStreamingResponse(client.models)


Client = HyperBee

AsyncClient = AsyncHyperBee