# Week 2 — Distributed Tracing

* I set  the API key for Honeycomb in my gitpod environment 
    `export HONEYCOMB_API_KEY="XXX"`
    `gp env HONEYCOMB_API_KEY="XXX"`
    `export HONEYCOMB_SERVICE_NAME="Cruddur"`
    `gp env HONEYCOMB_SERVICE_NAME="Cruddur"`


* Added env vars to the `docker-compose.yml` file
    * Open Telemetry to send to Honeycomb
    
    `OTEL_SERVICE_NAME: "backend-flask"`
    `OTEL_EXPORTER_OTLP_ENDPOINT: "https://api.honeycomb.io"`
    `OTEL_EXPORTER_OTLP_HEADERS: "x-honeycomb-team=${HONEYCOMB_API_KEY}"`

* Added Open Telemetry Python dependencies to `requirements.txt`

```
opentelemetry-api 
opentelemetry-sdk 
opentelemetry-exporter-otlp-proto-http 
opentelemetry-instrumentation-flask 
opentelemetry-instrumentation-requests
```

* Added to `backend/app.py`:

```py
# Honeycomb
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
```

```py
# Initialize automatic instrumentation with Flask
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()
```

* X Ray

  * Added to the requirements.txt: `aws-xray-sdk`

  * Added to app.py

    ```
    from aws_xray_sdk.core import xray_recorder
    from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

    xray_url = os.getenv("AWS_XRAY_URL")
    xray_recorder.configure(service='Cruddur', dynamic_naming=xray_url)
    XRayMiddleware(app, xray_recorder)
    ```

  * Added aws/json/xray.json

  * Created X Ray group

    ```  
    aws xray create-group \
    --group-name "backend-flask" \
    --filter-expression "service(\"backend-flask\") {fault OR error}"
    ```

  * Created sampling rule: `aws xray create-sampling-rule --cli-input-json file://aws/json/xray.json`   

  * Added daemon service to docker compose

    ```
    xray-daemon:
    image: "amazon/aws-xray-daemon"
    environment:
      AWS_ACCESS_KEY_ID: "${AWS_ACCESS_KEY_ID}"
      AWS_SECRET_ACCESS_KEY: "${AWS_SECRET_ACCESS_KEY}"
      AWS_REGION: "us-east-1"
    command:
      - "xray -o -b xray-daemon:2000"
    ports:
      - 2000:2000/udp
    ```

  * Added ENV variables to docker compose

  ```
    AWS_XRAY_URL: "*4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}*"
    AWS_XRAY_DAEMON_ADDRESS: "xray-daemon:2000"
  ```
  