# Frontend Design Documentation

How Google documents frontend design and web development. Grounded in [web.dev Learn Responsive Design](https://web.dev/learn/design), [Learn Accessibility](https://web.dev/learn/accessibility), and [Accessibility for a content-driven web app frontend](https://developers.google.com/solutions/content-driven/frontend/accessibility).

## Guide structure

Structure a frontend guide as a course or tutorial, one module per concern:

1. **Overview** — what the guide covers and the outcome for the reader.
2. **Layout** — macro layouts (page structure) and micro layouts (reusable components).
3. **Responsive design** — media queries, breakpoints, and flexible grids.
4. **Typography** — type scale, legibility, and readable line lengths.
5. **Images and icons** — responsive images and scalable iconography.
6. **Theming** — dark mode and user-preference adaptation.
7. **Accessibility** — semantic HTML, keyboard focus, contrast, alt text.
8. **Interaction** — mouse, keyboard, and touch input support.
9. **Performance** — budgets, lazy loading, and Core Web Vitals.
10. **Checklist** — a runnable review list.

## Responsive design rules

- Design mobile-first, then adapt upward with media queries.
- Give concrete breakpoint values and show the `@media` rule.
- Use flexible layouts (grid, flexbox) rather than fixed pixel widths.
- Use responsive images: `srcset`, `sizes`, and the `picture` element. State the benefit of each.

```css
@media (min-width: 768px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
```

## Accessibility rules

- Use semantic HTML elements for structure and forms; add ARIA only when a semantic element does not exist.
- Make every interactive element focusable and give it a visible focus indicator.
- Label every form field with a `<label>`; use `aria-label` for custom controls.
- Provide descriptive alt text for images; use `alt=""` for decorative images.
- Meet WCAG contrast guidelines (at least `4.5:1` for body text).
- Support keyboard-only navigation: the focus order must follow the DOM order.

## Form best practices

Use the same conventions as [Sign-in form best practices](https://web.dev/articles/sign-in-form-best-practices):

- Use meaningful elements: `<form>`, `<input>`, `<label>`, and `<button>`.
- Label each input with a `<label>`.
- Use built-in attributes: `type`, `name`, `autocomplete`, `required`.
- Keep `name` and `id` values stable across deploys.
- Do not disable the submit button while awaiting user input; explain missing input instead.

## Code sample conventions

- Show complete, self-contained HTML/CSS/JS snippets with realistic class names.
- Prefer progressive enhancement: the page must work without JavaScript.
- Annotate non-obvious lines with inline comments.
