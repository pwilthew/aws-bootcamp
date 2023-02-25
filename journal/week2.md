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