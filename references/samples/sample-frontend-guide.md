# Sample frontend design guide: Make your site responsive

This document is a representative complete frontend design guide, written in the web.dev Learn Responsive Design style. Use it as a template when writing frontend documentation.

## Overview

This guide shows you how to make a site that looks great and works well on every screen size, from a narrow phone to a wide desktop monitor. You learn to build layouts with CSS grid, adapt them with media queries, and make the result accessible and fast.

## Before you begin

- Basic knowledge of HTML and CSS.
- A browser with responsive design mode, such as Chrome DevTools.

## Design the macro layout

Start with the overall page structure. Define the main regions as a grid so the page reflows as the viewport changes.

```css
.page {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}

@media (min-width: 768px) {
  .page {
    grid-template-columns: 240px 1fr;
  }
}

@media (min-width: 1200px) {
  .page {
    grid-template-columns: 240px 1fr 300px;
  }
}
```

This layout starts as a single column on phones, adds a sidebar at `768px`, and adds an aside column at `1200px`.

## Build responsive components

Design micro layouts so components work in any location. Use `repeat(auto-fit, minmax(...))` so components fill available space without media queries.

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 16px;
}
```

## Use responsive images

Give visitors the most appropriate image for their device. Use `srcset` and `sizes` to let the browser choose.

```html
<img
  src="photo-800.jpg"
  srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1200.jpg 1200w"
  sizes="(min-width: 768px) 50vw, 100vw"
  alt="A mountain lake at sunrise">
```

Use the `picture` element to serve different formats, such as WebP with a JPEG fallback.

## Support dark mode

Adapt the design to the user's preference with the `prefers-color-scheme` media query.

```css
:root {
  color-scheme: light dark;
}

@media (prefers-color-scheme: dark) {
  :root {
    --background: #121212;
    --text: #e0e0e0;
  }
}
```

## Make it accessible

- Use semantic HTML: `<header>`, `<nav>`, `<main>`, and `<footer>` for landmarks.
- Make every interactive element focusable with a visible focus ring.
- Provide descriptive alt text for meaningful images and `alt=""` for decorative images.
- Meet WCAG contrast guidelines of at least `4.5:1` for body text.
- Support keyboard-only navigation; the focus order must follow the DOM order.

## Interaction

Support mouse, keyboard, and touch input. Do not rely on hover alone to reveal actions, because touch users cannot hover.

## Performance checklist

- Lazy-load images below the fold with `loading="lazy"`.
- Set `width` and `height` attributes on images to prevent layout shift.
- Audit the page with Lighthouse and address the Core Web Vitals.

## What's next

- [Learn Accessibility](https://web.dev/learn/accessibility) to go deeper on inclusive design.
- [Learn Performance](https://web.dev/learn/performance) to optimize page speed.
