from threading import current_thread
import time

class TimingMiddleware:
    def __init__(self):
        self.requests = {}
        self.count = 0

    def process_request(self, request):
        thread = current_thread()

        self.requests[thread] = {
            "Total": time.clock()
        }

        return None

    def process_response(self, request, response):
        thread = current_thread()

        if thread in self.requests:
            times = self.requests[thread]
            del self.requests[thread]
            for (key, value) in times.items():
                response["X-Time-" + key] = "%f" % (time.clock() - value)

        self.count = self.count + 1
        response["X-Requests"] = "%d" % self.count

        return response
