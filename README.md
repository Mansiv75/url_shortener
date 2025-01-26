# URL Shortener with Analytics

## Overview
This is a URL Shortener application built with **Django**, **Redis**, and **Docker**, deployed on **Render**. It allows users to shorten long URLs and tracks analytics, such as hit count and last accessed timestamps for each shortened URL.

## Features
- **Fast URL Redirection:** Utilizes Redis for caching URL mappings to ensure quick redirections.
- **Analytics Tracking:** Tracks hit count and last accessed timestamps for each shortened URL.
- **Admin Dashboard (Optional):** A dashboard for administrators to view real-time analytics.
- **Dockerized Deployment:** Easily deployable using Docker and Docker Compose.
- **Live Hosting:** Hosted on Render for seamless accessibility.

## Tech Stack
- **Backend Framework:** Django
- **Caching & Analytics:** Redis
- **Deployment:** Docker, Render
- **Frontend:** HTML, CSS

## Installation
Follow these steps to run the project locally:

### Prerequisites
- Python 3.10 or higher
- Docker & Docker Compose
- Redis (optional for local testing)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-link>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the `.env` file with the following variables:
   ```env
   REDIS_HOST=localhost
   REDIS_PORT=6380
   ```

4. Start Redis locally (if not using Docker):
   ```bash
   redis-server
   ```

5. Run the application:
   ```bash
   python manage.py runserver
   ```

6. Access the app at `http://127.0.0.1:8000/`.

### Running with Docker
1. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```

2. Access the app at `http://127.0.0.1:8000/`.

## API Endpoints
### 1. Shorten a URL
- **Endpoint:** `/`
- **Method:** `POST`
- **Payload:** `{ "url": "<original_url>" }`
- **Response:**
  ```json
  {
      "shortened_url": "<shortened_url>"
  }
  ```

### 2. Redirect to Original URL
- **Endpoint:** `/<shortened_url>/`
- **Method:** `GET`
- **Response:** Redirects to the original URL.

### 3. Analytics for a Shortened URL
- **Endpoint:** `/<shortened_url>/analytics/`
- **Method:** `GET`
- **Response:**
  ```json
  {
      "shortened_url": "<shortened_url>",
      "hit_count": "<number_of_hits>",
      "last_accessed": "<timestamp>"
  }
  ```

## Deployment
This project is live and hosted on Render.

### Deployment Steps
1. Ensure the project is Dockerized using the provided `Dockerfile` and `docker-compose.yml`.
2. Push the repository to a GitHub repository.
3. Connect the GitHub repository to Render.
4. Configure environment variables on Render.
5. Deploy the application.

## Usage
1. Enter the URL you want to shorten in the input field on the home page.
2. Click "Shorten URL" to get a shortened version.
3. Use the shortened URL to redirect to the original link.
4. Visit `/analytics/` for detailed statistics about your shortened URLs.

## Future Enhancements
- Add user authentication for personalized dashboards.
- Implement rate limiting using Redis.
- Provide graphical analytics for better insights.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- [Django Documentation](https://docs.djangoproject.com/)
- [Redis Documentation](https://redis.io/docs/)
- [Render Deployment Guides](https://render.com/docs)

---
### Live Project
🌐 **Live URL:** https://url-shortener-lv88.onrender.com 
📂 **GitHub Repository:** https://github.com/Mansiv75/url_shortener/

