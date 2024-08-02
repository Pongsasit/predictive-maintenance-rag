# Use an official Python runtime as a parent image
FROM  max003003003/genai:tmg-base-latest

# Set working directory
WORKDIR /usr/src/app

# Copy the application files
COPY .. .

RUN touch .env
# Set environment variables
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Configure Streamlit
RUN mkdir -p /.streamlit \
    && mkdir -p cache \
    && mkdir -p tmp \
    && chmod 777 /.streamlit \
    && echo "[general]\nemail = \"\"\n" > /.streamlit/credentials.toml \
    && echo "[server]\nenableCORS = false\nenableXsrfProtection = false\nenableWebsocketCompression = false\n" > /.streamlit/config.toml

# Expose port
EXPOSE 8080


CMD /bin/bash -c "python -m streamlit run app.py --server.port=8080"