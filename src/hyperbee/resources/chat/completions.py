# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional, overload, Tuple, Any
from typing_extensions import Literal

import httpx
import time
import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..._client import HyperBee, AsyncHyperBee

from openai import _legacy_response
from openai._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from openai._utils import required_args, maybe_transform
from openai._compat import cached_property
from openai._resource import SyncAPIResource, AsyncAPIResource
from openai._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from openai._streaming import Stream, AsyncStream
from openai.types.chat import (
    ChatCompletion,
    ChatCompletionChunk,
    ChatCompletionToolParam,
    ChatCompletionMessageParam,
    ChatCompletionToolChoiceOptionParam,
    completion_create_params,
)
from openai._base_client import (
    make_request_options,
)

__all__ = ["Completions", "AsyncCompletions"]


class Completions(SyncAPIResource):
    _client: "HyperBee"  # Use string annotation to avoid circular import
    __COLLECTIONS = "bee_collections"

    @cached_property
    def with_raw_response(self) -> CompletionsWithRawResponse:
        return CompletionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsWithStreamingResponse:
        return CompletionsWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[
            str,
            Literal["hyperchat",],
        ],
        namespace: Optional[str] | NotGiven = NOT_GIVEN,
        optimization: Optional[Literal["fast", "premium", "auto"]] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        output_mode: Optional[str] | NotGiven = NOT_GIVEN,
        json_schema: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion:
        """ """
        ...

    @overload
    def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[
            str,
            Literal["hyperchat",],
        ],
        stream: Literal[True],
        namespace: Optional[str] | NotGiven = NOT_GIVEN,
        max_num_results: Optional[int] | NotGiven = NOT_GIVEN,
        optimization: Optional[Literal["fast", "premium", "auto"]] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        output_mode: Optional[str] | NotGiven = NOT_GIVEN,
        json_schema: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[ChatCompletionChunk]:
        """ """
        ...

    @overload
    def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[
            str,
            Literal["hyperchat",],
        ],
        stream: bool,
        namespace: Optional[str] | NotGiven = NOT_GIVEN,
        max_num_results: Optional[int] | NotGiven = NOT_GIVEN,
        optimization: Optional[Literal["fast", "premium", "auto"]] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        output_mode: Optional[str] | NotGiven = NOT_GIVEN,
        json_schema: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion | Stream[ChatCompletionChunk]:
        """ """
        ...

    @required_args(["messages", "model"], ["messages", "model", "stream"])
    def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[
            str,
            Literal["hyperchat",],
        ],
        namespace: Optional[str] | NotGiven = NOT_GIVEN,
        max_num_results: Optional[int] | NotGiven = NOT_GIVEN,
        optimization: Optional[Literal["fast", "premium", "auto"]] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        output_mode: Optional[str] | NotGiven = NOT_GIVEN,
        json_schema: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion | Stream[ChatCompletionChunk]:
        """Creates a model response for the given chat conversation.

        Args:
          messages: A list of messages comprising the conversation so far.
              [Example Python code](https://cookbook.openai.com/examples/how_to_format_inputs_to_chatgpt_models).

          model: ID of the model to use. See the
              For now only `hive` is supported.

          namespace: The namespace to use for the request.

          max_num_results: The maximum number of results to include in the context.

          optimization: Whether to optimize for `cost` or `quality`. If set to `auto`,
              the API will optimize for both cost and quality. The default is `auto`.

          stream: If set, partial message deltas will be sent, like in ChatGPT. Tokens will be
              sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.
              [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

              [See more information about frequency and presence penalties.](https://platform.openai.com/docs/guides/text-generation/parameter-details)

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`. This option is currently not available on the `gpt-4-vision-preview`
              model.

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion.

              The total length of input tokens and generated tokens is limited by the model's
              context length.
              [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken)
              for counting tokens.

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

              [See more information about frequency and presence penalties.](https://platform.openai.com/docs/guides/text-generation/parameter-details)

          response_format: An object specifying the format that the model must output. Compatible with
              [GPT-4 Turbo](https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo) and
              all GPT-3.5 Turbo models newer than `gpt-3.5-turbo-1106`.

              Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the
              message the model generates is valid JSON.

              **Important:** when using JSON mode, you **must** also instruct the model to
              produce JSON yourself via a system or user message. Without this, the model may
              generate an unending stream of whitespace until the generation reaches the token
              limit, resulting in a long-running and seemingly "stuck" request. Also note that
              the message content may be partially cut off if `finish_reason="length"`, which
              indicates the generation exceeded `max_tokens` or the conversation exceeded the
              max context length.

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          stop: Up to 4 sequences where the API will stop generating further tokens.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

              We generally recommend altering this or `top_p` but not both.

          tool_choice: Controls which (if any) function is called by the model. `none` means the model
              will not call a function and instead generates a message. `auto` means the model
              can pick between generating a message or calling a function. Specifying a
              particular function via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for.

          top_logprobs: An integer between 0 and 5 specifying the number of most likely tokens to return
              at each token position, each with an associated log probability. `logprobs` must
              be set to `true` if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help OpenAI to monitor
              and detect abuse.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids).

          output_mode: Specifies the desired output format for the model's response.
              If set to "json", the model will attempt to generate a valid JSON response.
              Otherwise, the model will generate a regular text response.

          json_schema: Specifies a JSON schema that the model's JSON response should conform to.
            The schema should be a Python dictionary following the JSON Schema specification (https://json-schema.org/).
            If not provided, the model will generate a JSON response without enforcing a specific schema.


          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds"""

        if namespace is not NOT_GIVEN:
            self._client.set_base_url_for_request(namespace)
        else:
            self._client.set_base_url_for_request(None)

        return self._post(
            "/chat/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "frequency_penalty": frequency_penalty,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "n": n,
                    "presence_penalty": presence_penalty,
                    "response_format": response_format,
                    "seed": seed,
                    "stop": stop,
                    "stream": stream,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "user": user,
                    "namespace": namespace,
                    "max_num_results": max_num_results,
                    "optimization": optimization,
                    "output_mode": output_mode,
                    "json_schema": json_schema,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletion,
            stream=stream or False,
            stream_cls=Stream[ChatCompletionChunk],
        )

    def __file_upload(
        self, folderpath: str, filename: str, namespace: Optional[str] | None, collection_name: str
    ) -> Tuple[str, str, str]:
        """
        Uploads a single file to a specified namespace or creates a new namespace if none is provided.

        This function uploads a file from a given folder path and filename to a specified namespace.
        If the namespace is None, a new namespace is created. The function returns the namespace ID,
        contact email, and a message from the server upon successful upload. If the API response is
        not successful (status code other than 200), a ValueError is raised.

        Args:
            folderpath (str): The path to the folder containing the file to be uploaded.
            filename (str): The name of the file to be uploaded.
            namespace (Optional[str] | None): The namespace to which the file should be uploaded.
                                              If None, a new namespace is created.
            collection_name (str): The name of the collection to which the file belongs.

        Returns:
            Tuple[str, str, str]: A tuple containing the namespace ID, contact email, and a message
                                  from the server.

        Raises:
            ValueError: If the API response is not successful (status code other than 200).
        """
        filepath = os.path.join(folderpath, filename)  # to make this platform-independent, i.e., avoid / vs \
        with open(filepath, "rb") as filedata:
            data = {"bucket_name": self.__COLLECTIONS, "name": collection_name}
            if namespace is not None:
                data["namespace"] = namespace

            response = httpx.post(
                url=f"{self._client.base_url}upload",
                files={"file": (filename, filedata)},
                headers={"Authorization": f"Bearer {self._client.api_key}"},
                data=data,
            )
            if response.status_code == 200:
                response_json = response.json()  # Use the built-in JSON decoder
                response_collection_namespace = response_json.get("namespace")
                response_contact_mail = response_json.get("contact_mail")
                response_message = response_json.get("message")
            else:
                raise ValueError(f"Response from remote ({response.status_code}): {response.text}")

        return response_collection_namespace, response_contact_mail, response_message

    def get_remote_doclist(self, namespace: str) -> List[str]:
        """
        Fetches the list of documents available in a specified remote namespace.

        Args:
            namespace (str): The identifier of the namespace from which to fetch the document list.

        Returns:
            List[str]: A list of document names available in the specified namespace.

        Raises:
            ValueError: If the namespace ID is None, if the document list is empty, or if the API response
                        is not successful (status code other than 200).
        """
        if self._client.base_url != self._client._rag_base_url:
            self._client.set_base_url_for_request(namespace)

        with httpx.Client() as client:
            response = client.post(
                url=f"{self._client.base_url}document_list",
                headers={"Authorization": f"Bearer {self._client.api_key}"},
                json={"namespace": namespace, "contact_mail": "random@gmail.com"},
            )

        if response.status_code == 200:
            remote_doclist = response.json()
        else:
            raise ValueError(f"Response from remote ({response.status_code}): {response.text}")

        if not isinstance(remote_doclist, list):
            errmsg = "Either a namespace with this ID does not exist, or the namespace only has non-indexed files. "
            errmsg += "Please contact librarian@hyperbee.ai if you think you should not have received this error."
            raise ValueError(errmsg)

        return remote_doclist

    def __update_index(self, namespace: str, contact_mail: str) -> dict[str, Any]:
        """
        Updates the bucket index after an upload or deletion and runs embedding.

        Args:
            namespace (str): The namespace identifier for which the index needs to be updated.
            contact_mail (str): The contact email associated with the request.

        Returns:
            dict[str, Any]: A dictionary containing the response message from the server.

        Raises:
            ValueError: If the response from the server is not successful (status code other than 200).
        """
        response = httpx.post(
            url=f"{self._client.base_url}update",
            headers={"Authorization": f"Bearer {self._client.api_key}"},
            json={"namespace": namespace, "contact_mail": contact_mail},
        )
        if response.status_code == 200:
            response_message = response.json()  # Use the built-in JSON decoder
        else:
            raise ValueError(f"Response from remote ({response.status_code}): {response.text}")

        return response_message

    def __poll_collection_index(
        self,
        local_doclist: List[str],
        namespace: str,
        checkfilter: Literal["sync", "add", "remove"],
        sleepseconds: int = 2,
        timeoutseconds: int = 120,
        verbose: bool = False,
    ) -> bool:

        stop_trying = False
        timeout_flag = False
        start_time = time.time()
        while not stop_trying:
            remote_doclist = self.get_remote_doclist(namespace=namespace)
            if verbose:
                print("Remote: ", remote_doclist)
                print("Local:  ", local_doclist)
                print(
                    f"Checking for index completion every {sleepseconds} s, Timeout = {timeoutseconds} s. Elapsed: {time.time() - start_time:.2f} seconds"
                )
            else:
                print(
                    f"Checking for index completion every {sleepseconds} s, Timeout = {timeoutseconds} s. Elapsed: {time.time() - start_time:.2f} seconds",
                    end="\r",
                    flush=True,
                )

            # apply checkfilter
            if checkfilter == "sync":
                if set(local_doclist) == set(remote_doclist):  # := if local and remote match exactly
                    stop_trying = True
            elif checkfilter == "add":
                if set(local_doclist) <= set(remote_doclist):  # := if local (uploaded) a subset of remote
                    stop_trying = True
            elif checkfilter == "remove":
                if not set(local_doclist) & set(
                    remote_doclist
                ):  # := if local (deleted) is not an element of remote anymore
                    stop_trying = True

            # timeout mechanism
            if (time.time() - start_time) > timeoutseconds:
                stop_trying = True
                timeout_flag = True

            # wait a bit to not hog processors
            time.sleep(sleepseconds)

        if timeout_flag:
            print(
                "\nIndexing check did not complete up to now. Call poll_index() again later to see if it's completed."
            )
            return False
        else:
            print("\nIndexing check complete. Checkfilter conditions are met.")
            return True

    def __update_deleted_items(self, namespace: str) -> Dict[str, Any]:
        """
        Updates the namespace after items have been deleted.

        Args:
            namespace: The namespace ID.

        Returns:
            Dict[str, Any]: The response message from the API.

        Raises:
            ValueError: If namespace is None.
        """
        with httpx.Client() as client:
            response = client.post(
                url=f"{self._client.base_url}delete",
                headers={"Authorization": f"Bearer {self._client.api_key}"},
                json={"namespace": namespace},
            )

        if response.status_code == 200:
            response_message = response.json()
        else:
            raise ValueError(f"Response from remote ({response.status_code}): {response.text}")

        return response_message

    def __file_delete_from_bucket(self, namespace: str, delete_list: List[str]) -> Dict[str, Any]:
        """
        Deletes a list of files from a namespace (not the index, the bucket).

        Args:
            namespace: The namespace ID.
            delete_list: List of files to delete.

        Returns:
            Dict[str, Any]: The response message from the API.

        Raises:
            ValueError: If namespace is None or delete_list is empty.
        """
        if not delete_list:
            raise ValueError(
                "Parameter *delete_list* cannot be empty while deleting files from a namespace. Please provide a valid list."
            )

        with httpx.Client() as client:
            response = client.post(
                url=f"{self._client.base_url}delete_from_bucket",
                headers={"Authorization": f"Bearer {self._client.api_key}"},
                json={"namespace": namespace, "delete_list": delete_list},
            )

        if response.status_code == 200:
            response_message = response.json()
        else:
            raise ValueError(f"Response from remote ({response.status_code}): {response.text}")

        return response_message

    def __get_local_doclist(self, folder_path: str) -> List[str]:
        """
        Get a list of supported documents from a local folder.

        Args:
            folder_path: The path to the folder containing the documents.

        Returns:
            List[str]: A list of supported document filenames.

        Raises:
            ValueError: If a file has no extension or an unsupported extension.
        """
        supported_extensions = ["pdf", "txt"]
        local_document_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        for document_filename in local_document_list:
            document_filename_components = document_filename.split(".")
            if len(document_filename_components) == 1:
                raise ValueError(f"File {document_filename} does not have a file extension, which is not allowed.")

            extension = document_filename_components[-1]
            if extension not in supported_extensions:
                supported_extensions_str = ", ".join(supported_extensions)
                raise ValueError(
                    f'File {document_filename} has unsupported extension "{extension}". Supported extensions are: [{supported_extensions_str}]'
                )

        return local_document_list

    def create_namespace(
        self, file_list: List[str], sleepseconds: int = 10, timeoutseconds: int = 60, verbose: bool = True
    ) -> str:
        """
        Create a new namespace by uploading a list of files.

        Args:
            file_list (List[str]): A list of file paths to be uploaded to create the namespace.
            sleepseconds (int, optional): The number of seconds to sleep between polling attempts. Defaults to 10.
            timeoutseconds (int, optional): The maximum time in seconds to wait for the operation to complete. Defaults to 60.
            verbose (bool, optional): If True, prints detailed output during the operation. Defaults to True.

        Returns:
            str: The created namespace identifier. Returns an empty string if the creation fails.

        Raises:
            ValueError: If the namespace creation fails.
        """
        try:
            namespace = self.add_to_collection(
                file_list,
                None,
                sleepseconds=sleepseconds,
                timeoutseconds=timeoutseconds,
                verbose=verbose,
                approved=True,
            )
        except Exception as e:
            print(f"Failed to create namespace: {str(e)}")
            return ""

        if namespace is None:
            raise ValueError("Failed to create namespace")
        else:
            return namespace

    def add_to_collection(
        self,
        uploadlist: List[str],
        namespace: str | None,
        sleepseconds: int = 2,
        timeoutseconds: int = 60,
        verbose: bool = False,
        approved: bool = False,
    ) -> None | Tuple[str, str]:
        """
        Add documents to a collection in the specified namespace.

        Args:
            uploadlist: List of file paths to upload.
            namespace: The namespace to add the documents to.
            sleepseconds: Sleep time between polling attempts (default: 2).
            timeoutseconds: Timeout for the entire operation in seconds (default: 60).
            verbose: Whether to print verbose output (default: False).
        """
        if self._client.base_url != self._client._rag_base_url:
            self._client.set_base_url_for_request("placeholder")

        user_choice = False
        if namespace is not None:
            remote_doclist = self.get_remote_doclist(namespace=namespace)

            # Extract filenames from uploadlist
            uploadlist_filenames = [os.path.basename(file) for file in uploadlist]

            filesInUploadList_butNotInRemote = list(set(uploadlist_filenames) - set(remote_doclist))
            filesThatAlreadyExistInRemote = list(set(uploadlist_filenames) - set(filesInUploadList_butNotInRemote))
            print("Files in local but not in remote (to be uploaded):", filesInUploadList_butNotInRemote)

            if len(filesThatAlreadyExistInRemote) > 0:
                print(
                    "The following files already exist in remote, so they will not be uploaded at this time:",
                    filesThatAlreadyExistInRemote,
                )
                print(
                    "You need to delete the current version of these files from the collection (using remove_from_collection()) before uploading its next version"
                )
                if len(filesInUploadList_butNotInRemote) == 0:
                    print("Nothing to upload, canceling.")
                    return
            print("")

            if not approved:
                user_decision = input(
                    "Please check the lists above. Do you want to continue with the upload? (answer with just y or n)"
                )
                user_choice = user_decision.lower() == "y"
            if len(filesInUploadList_butNotInRemote) == 0:
                if verbose:
                    print("No files to be uploaded, skipping file upload to remote")
                return
        else:
            filesInUploadList_butNotInRemote = [os.path.basename(file) for file in uploadlist]

        if approved or user_choice:
            contact_mail = None
            received_namespace = ""
            ### route /upload canNOT be called with a file list, needs to iterate over list
            for file in uploadlist:
                if os.path.basename(file) in filesInUploadList_butNotInRemote:
                    folderpath, filename = os.path.split(file)
                    received_namespace, contact_mail, _ = self.__file_upload(
                        folderpath, filename, namespace=namespace, collection_name="dummy"
                    )  # collection_name is not needed for existing collections

            if contact_mail is not None:
                self.__update_index(namespace=received_namespace, contact_mail=contact_mail)
            else:
                raise Exception("File upload error")

            print(
                "Upload and indexing update triggered, starting to poll the indexing mechanism with check_index_completion() ..."
            )
            print("")
            success = self.__poll_collection_index(
                local_doclist=filesInUploadList_butNotInRemote,
                namespace=received_namespace,
                checkfilter="add",
                sleepseconds=sleepseconds,
                timeoutseconds=timeoutseconds,
                verbose=verbose,
            )
            status = "Ready" if success else "Pending"
            if namespace is None:
                return received_namespace, status
        else:
            print("Canceling upload")

    def __delete_all_documents(self, namespace: str) -> None:
        """
        Deletes all documents within the specified namespace.

        Args:
            namespace (str): The namespace from which all documents will be deleted.

        Raises:
            ValueError: If the server response indicates a failure to delete the documents.
        """
        with httpx.Client() as client:
            response = client.post(
                url=f"{self._client.base_url}delete_all_document",
                headers={"Authorization": f"Bearer {self._client.api_key}"},
                json={"namespace": namespace},
            )

        if response.status_code != 200:
            raise ValueError(f"Response from remote ({response.status_code}): {response.text}")

    def __delete_all_from_vectorstore(self, namespace: str) -> None:
        """
        Deletes all entries from the vector store associated with the specified namespace.

        Args:
            namespace (str): The namespace from which all entries will be deleted.

        Raises:
            ValueError: If the server response indicates a failure to delete the entries.
        """
        with httpx.Client() as client:
            response = client.post(
                url=f"{self._client.base_url}delete",
                headers={"Authorization": f"Bearer {self._client.api_key}"},
                json={"namespace": namespace},
            )

        if response.status_code != 200:
            raise ValueError(f"Response from remote ({response.status_code}): {response.text}")

    def delete_namespace(self, namespace: str) -> None:
        """
        Deletes all documents and entries associated with the specified namespace.

        This function attempts to delete all documents within the given namespace
        and all entries from the vector store associated with the namespace. If any
        deletion operation fails, an error message is printed.

        Args:
            namespace (str): The identifier of the namespace to be deleted.

        Raises:
            Exception: If an error occurs during the deletion of documents or vector store entries.
        """
        try:
            self.__delete_all_documents(namespace=namespace)
        except Exception as e:
            print(f"Failed to delete namespace: {str(e)}")
        try:
            self.__delete_all_from_vectorstore(namespace=namespace)
        except Exception as e:
            print(f"Failed to delete namespace: {str(e)}")

        print(f"Namespace {namespace} deleted")

    def remove_from_collection(
        self,
        deletionlist: List[str],
        namespace: str,
        sleepseconds: int = 2,
        timeoutseconds: int = 60,
        verbose: bool = False,
        approved: bool = False,
    ) -> None:
        """
        Removes files from an existing namespace.

        This method skips files that do not exist automatically and informs the user.
        It asks for user confirmation before deleting.

        Args:
            deletionlist (List[str]): List of files to be deleted.
            namespace (str): The namespace from which to remove files.
            sleepseconds (int, optional): Sleep time between polling attempts. Defaults to 2.
            timeoutseconds (int, optional): Timeout for polling in seconds. Defaults to 60.
            verbose (bool, optional): If True, prints verbose output. Defaults to False.

        Raises:
            ValueError: If namespace is None.
        """
        if self._client.base_url != self._client._rag_base_url:
            self._client.set_base_url_for_request(namespace)
        remote_doclist = self.get_remote_doclist(namespace=namespace)

        deletelist_filenames = [os.path.basename(file) for file in deletionlist]

        filesInRemote_matchingDeletionList = set(deletelist_filenames).intersection(set(remote_doclist))
        if len(filesInRemote_matchingDeletionList) == 0:
            print("No files to be deleted, skipping file deletion from remote")
            return
        print("Files in remote that will be deleted:", list(filesInRemote_matchingDeletionList))
        filesInDeletionList_butNotInCollection = set(deletelist_filenames) - filesInRemote_matchingDeletionList
        if filesInDeletionList_butNotInCollection:
            print(
                "The following files do not exist in remote, so they cannot be deleted at this time:",
                list(filesInDeletionList_butNotInCollection),
            )

        print("")
        user_choice = False
        if not approved:
            user_decision = input(
                "Please check the lists above. Do you want to continue with the deletion? (answer with just y or n)"
            )
            user_choice = user_decision.lower() == "y"

        if approved or user_choice:
            self.__file_delete_from_bucket(namespace=namespace, delete_list=list(filesInRemote_matchingDeletionList))
            self.__update_deleted_items(namespace=namespace)

            print(
                "Deletion and indexing update triggered, starting to poll the indexing mechanism with check_index_completion() ..."
            )
            print("")
            local_list_for_polling = list(filesInRemote_matchingDeletionList)
            _ = self.__poll_collection_index(
                local_doclist=local_list_for_polling,
                namespace=namespace,
                checkfilter="remove",
                sleepseconds=sleepseconds,
                timeoutseconds=timeoutseconds,
                verbose=verbose,
            )
        else:
            print("Canceling deletion")
            return

    ### Syncs local and remote folders if there are any differences between them
    def sync_local_and_collection(
        self, folder_path: str, namespace: str, sleepseconds: int = 2, timeoutseconds: int = 60, verbose: bool = False
    ) -> None:
        """
        Syncs local and remote folders if there are any differences between them.

        This method asks the user for input after listing the deltas since sync is a potentially catastrophic action on the remote side.
        Local files always win, remote gets modified accordingly.

        Args:
            folder_path (str): Path to the local folder.
            namespace (str): The namespace to sync with.
            sleepseconds (int, optional): Sleep time between polling attempts. Defaults to 2.
            timeoutseconds (int, optional): Timeout for polling in seconds. Defaults to 60.
            verbose (bool, optional): If True, prints verbose output. Defaults to False.

        Returns:
            bool: True if sync was successful, False otherwise.

        Raises:
            ValueError: If namespace is None.
        """
        if self._client.base_url != self._client._rag_base_url:
            self._client.set_base_url_for_request(namespace)
        remote_doclist = self.get_remote_doclist(namespace=namespace)
        local_doclist_filenames = self.__get_local_doclist(folder_path=folder_path)
        local_doclist = [os.path.join(folder_path, file) for file in local_doclist_filenames]

        files_to_delete = list(set(remote_doclist) - set(local_doclist_filenames))
        files_to_upload = list(set(local_doclist_filenames) - set(remote_doclist))

        print("Files in remote but not in local (to be deleted):", files_to_delete)
        print("Files in local but not in remote (to be uploaded):", files_to_upload)

        print("")
        user_decision = input(
            "Please check the lists above. Do you want to continue with the sync? (answer with just y or n)"
        )

        if user_decision.lower() == "y":
            if files_to_delete:
                self.remove_from_collection(
                    deletionlist=files_to_delete,
                    namespace=namespace,
                    sleepseconds=sleepseconds,
                    timeoutseconds=timeoutseconds,
                    verbose=verbose,
                    approved=True,
                )
            if files_to_upload:
                self.add_to_collection(
                    uploadlist=[file for file in local_doclist if os.path.basename(file) in files_to_upload],
                    namespace=namespace,
                    sleepseconds=sleepseconds,
                    timeoutseconds=timeoutseconds,
                    verbose=verbose,
                    approved=True,
                )
        else:
            print("Canceling sync")


class AsyncCompletions(AsyncAPIResource):
    _client: "AsyncHyperBee"

    @cached_property
    def with_raw_response(self) -> AsyncCompletionsWithRawResponse:
        return AsyncCompletionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsWithStreamingResponse:
        return AsyncCompletionsWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[
            str,
            Literal["hyperchat",],
        ],
        namespace: Optional[str] | NotGiven = NOT_GIVEN,
        optimization: Optional[Literal["fast", "premium", "auto"]] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        output_mode: Optional[str] | NotGiven = NOT_GIVEN,
        json_schema: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion:
        """ """
        ...

    @overload
    async def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[
            str,
            Literal["hyperchat",],
        ],
        stream: Literal[True],
        namespace: Optional[str] | NotGiven = NOT_GIVEN,
        optimization: Optional[Literal["fast", "premium", "auto"]] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        output_mode: Optional[str] | NotGiven = NOT_GIVEN,
        json_schema: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[ChatCompletionChunk]:
        """ """
        ...

    @overload
    async def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[
            str,
            Literal["hyperchat",],
        ],
        stream: bool,
        namespace: Optional[str] | NotGiven = NOT_GIVEN,
        optimization: Optional[Literal["fast", "premium", "auto"]] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        output_mode: Optional[str] | NotGiven = NOT_GIVEN,
        json_schema: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion | AsyncStream[ChatCompletionChunk]:
        """ """
        ...

    @required_args(["messages", "model"], ["messages", "model", "stream"])
    async def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[
            str,
            Literal["hyperchat",],
        ],
        namespace: Optional[str] | NotGiven = NOT_GIVEN,
        optimization: Optional[Literal["fast", "premium", "auto"]] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        output_mode: Optional[str] | NotGiven = NOT_GIVEN,
        json_schema: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion | AsyncStream[ChatCompletionChunk]:
        """Creates a model response for the given chat conversation.

        Args:
          messages: A list of messages comprising the conversation so far.
              [Example Python code](https://cookbook.openai.com/examples/how_to_format_inputs_to_chatgpt_models).

          model: ID of the model to use. See the
              For now only `hive` is supported.

          namespace: The namespace to use for the request.

          optimization: Whether to optimize for `cost` or `quality`. If set to `auto`,
              the API will optimize for both cost and quality. The default is `auto`.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

              [See more information about frequency and presence penalties.](https://platform.openai.com/docs/guides/text-generation/parameter-details)

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`. This option is currently not available on the `gpt-4-vision-preview`
              model.

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion.

              The total length of input tokens and generated tokens is limited by the model's
              context length.
              [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken)
              for counting tokens.

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

              [See more information about frequency and presence penalties.](https://platform.openai.com/docs/guides/text-generation/parameter-details)

          response_format: An object specifying the format that the model must output. Compatible with
              [GPT-4 Turbo](https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo) and
              all GPT-3.5 Turbo models newer than `gpt-3.5-turbo-1106`.

              Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the
              message the model generates is valid JSON.

              **Important:** when using JSON mode, you **must** also instruct the model to
              produce JSON yourself via a system or user message. Without this, the model may
              generate an unending stream of whitespace until the generation reaches the token
              limit, resulting in a long-running and seemingly "stuck" request. Also note that
              the message content may be partially cut off if `finish_reason="length"`, which
              indicates the generation exceeded `max_tokens` or the conversation exceeded the
              max context length.

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          stop: Up to 4 sequences where the API will stop generating further tokens.

          stream: If set, partial message deltas will be sent, like in ChatGPT. Tokens will be
              sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.
              [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

              We generally recommend altering this or `top_p` but not both.

          tool_choice: Controls which (if any) function is called by the model. `none` means the model
              will not call a function and instead generates a message. `auto` means the model
              can pick between generating a message or calling a function. Specifying a
              particular function via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for.

          top_logprobs: An integer between 0 and 5 specifying the number of most likely tokens to return
              at each token position, each with an associated log probability. `logprobs` must
              be set to `true` if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help OpenAI to monitor
              and detect abuse.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids).

          output_mode: Specifies the desired output format for the model's response.
              If set to "json", the model will attempt to generate a valid JSON response.
              Otherwise, the model will generate a regular text response.

          json_schema: Specifies a JSON schema that the model's JSON response should conform to.
            The schema should be a Python dictionary following the JSON Schema specification (https://json-schema.org/).
            If not provided, the model will generate a JSON response without enforcing a specific schema.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds"""
        self._client.set_base_url_for_request(namespace)

        return await self._post(
            "/chat/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "frequency_penalty": frequency_penalty,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "n": n,
                    "presence_penalty": presence_penalty,
                    "response_format": response_format,
                    "seed": seed,
                    "stop": stop,
                    "stream": stream,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "user": user,
                    "namespace": namespace,
                    "optimization": optimization,
                    "output_mode": output_mode,
                    "json_schema": json_schema,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletion,
            stream=stream or False,
            stream_cls=AsyncStream[ChatCompletionChunk],
        )


class CompletionsWithRawResponse:
    def __init__(self, completions: Completions) -> None:
        self._completions = completions

        self.create = _legacy_response.to_raw_response_wrapper(
            completions.create,
        )


class AsyncCompletionsWithRawResponse:
    def __init__(self, completions: AsyncCompletions) -> None:
        self._completions = completions

        self.create = _legacy_response.async_to_raw_response_wrapper(
            completions.create,
        )


class CompletionsWithStreamingResponse:
    def __init__(self, completions: Completions) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )


class AsyncCompletionsWithStreamingResponse:
    def __init__(self, completions: AsyncCompletions) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
