import logging
from playwright.sync_api import APIRequestContext
import time

logger = logging.getLogger(__name__)


class APIClient:

    def __init__(self, request_context: APIRequestContext):

        self.request_context = request_context

        # Common headers for all API requests
        self.default_headers = {
            "Accept": "application/json"
        }

    # Common request handler
    
    def _send_request(
            self,
            method,
            endpoint,
            params=None,
            data=None,
            headers=None
        ):

        request_headers = {
        **self.default_headers,
        **(headers or {})
        }

        start_time = time.perf_counter()

        logger.info("REQUEST: %s %s", method, endpoint)

        try:
         response = self.request_context.fetch(
            endpoint,
            method=method,
            params=params,
            data=data,
            headers=request_headers
         )

         execution_time = (
            time.perf_counter() - start_time
         ) * 1000

         logger.info(
            "RESPONSE: %s | STATUS: %s | TIME: %.2f ms",
            endpoint,
            response.status,
            execution_time
          )

         return response

        except Exception:
         logger.exception(
            "API request failed: %s %s",
            method,
            endpoint
         )

         raise

    # GET
    def get(self, endpoint, params=None, headers=None):

        return self._send_request(
            "GET", endpoint,
            params=params,
            headers=headers
        )

    # POST
    def post(self, endpoint, data=None, headers=None):

        return self._send_request(
            "POST", endpoint,
            data=data,
            headers=headers
        )

    # PUT
    def put(self, endpoint, data=None, headers=None):

        return self._send_request(
            "PUT", endpoint,
            data=data,
            headers=headers
        )

    # PATCH
    def patch(self, endpoint, data=None, headers=None):

        return self._send_request(
            "PATCH", endpoint,
            data=data,
            headers=headers
        )

    # DELETE
    def delete(self, endpoint, headers=None):

        return self._send_request(
            "DELETE", endpoint,
            headers=headers
        )
