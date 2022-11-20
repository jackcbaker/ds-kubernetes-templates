from python:3.9


# Create virtualenv and point python
# to created venv python
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"


# Install scikit-learn dependency
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Fetch rest of app
COPY src/ ./src/

# Command to run by default in container
CMD python -m src.main