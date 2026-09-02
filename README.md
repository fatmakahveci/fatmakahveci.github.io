# fatmakahveci.com — Published Site

[![Website](https://img.shields.io/badge/Website-fatmakahveci.com-0F766E?logo=githubpages&logoColor=white)](https://fatmakahveci.com/)
[![GitHub Pages](https://img.shields.io/badge/Hosted%20with-GitHub%20Pages-222222?logo=github&logoColor=white)](https://pages.github.com/)
[![Last commit](https://img.shields.io/github/last-commit/fatmakahveci/fatmakahveci.github.io)](https://github.com/fatmakahveci/fatmakahveci.github.io/commits/main)

The GitHub Pages deployment repository for fatmakahveci.com, containing the generated HTML, feeds, assets, and topic archives served in production.

## Highlights

- Static production output for GitHub Pages
- Technical, research, reading, and travel sections
- RSS/XML feeds, sitemap, and social metadata
- Custom domain configuration through `CNAME`

## Technology

- GitHub Pages
- HTML
- CSS
- JavaScript

## Getting Started

### Prerequisites

- A browser for viewing the deployed site
- Python 3 for an optional local static server

### Installation

```bash
python3 -m http.server 8000
```

Open http://localhost:8000, or visit the production site at https://fatmakahveci.com.

## Repository Structure

- `index.html` — published home page
- `*-note` directories — generated topic archives
- `img`, `css`, and `js` — deployed assets
- `CNAME` — custom-domain mapping

## Project Resources

- [Changelog](CHANGELOG.md)
- [Contributing guide](.github/CONTRIBUTING.md)
- [Security policy](.github/SECURITY.md)
- [License](LICENSE.md)
