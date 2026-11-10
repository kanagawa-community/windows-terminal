<img align="left" src="https://raw.githubusercontent.com/kanagawa-community/.github/main/assets/branding/logo.png" alt="Kanagawa logo" width="200">

<h3>Kanagawa for <a href="https://github.com/microsoft/terminal">Windows Terminal</a></h3>
<p>A community-maintained theme inspired by Hokusai's <em>The Great Wave off Kanagawa</em>.</p>
<p>Using the <a href="https://github.com/rebelot/kanagawa.nvim">Kanagawa palette</a> by <a href="https://github.com/rebelot">Tommaso Laurenzi (rebelot)</a>.</p>

<!-- Wave accents: carpYellow, crystalBlue, autumnRed. Lotus accents: lotusYellow, lotusBlue4, lotusRed. -->
<p>
  <a href="https://github.com/kanagawa-community/windows-terminal/stargazers">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/github/stars/kanagawa-community/windows-terminal?style=for-the-badge&amp;labelColor=1F1F28&amp;color=E6C384">
      <source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/github/stars/kanagawa-community/windows-terminal?style=for-the-badge&amp;labelColor=F2ECBC&amp;color=77713F">
      <img src="https://img.shields.io/github/stars/kanagawa-community/windows-terminal?style=for-the-badge&amp;labelColor=1F1F28&amp;color=E6C384" alt="GitHub stars">
    </picture>
  </a>
  <a href="https://github.com/kanagawa-community/windows-terminal/releases/latest">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/github/v/release/kanagawa-community/windows-terminal?style=for-the-badge&amp;label=release&amp;labelColor=1F1F28&amp;color=7E9CD8">
      <source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/github/v/release/kanagawa-community/windows-terminal?style=for-the-badge&amp;label=release&amp;labelColor=F2ECBC&amp;color=4D699B">
      <img src="https://img.shields.io/github/v/release/kanagawa-community/windows-terminal?style=for-the-badge&amp;label=release&amp;labelColor=1F1F28&amp;color=7E9CD8" alt="Latest release">
    </picture>
  </a>
  <a href="https://github.com/kanagawa-community/windows-terminal/issues">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/github/issues/kanagawa-community/windows-terminal?style=for-the-badge&amp;labelColor=1F1F28&amp;color=C34043">
      <source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/github/issues/kanagawa-community/windows-terminal?style=for-the-badge&amp;labelColor=F2ECBC&amp;color=C84053">
      <img src="https://img.shields.io/github/issues/kanagawa-community/windows-terminal?style=for-the-badge&amp;labelColor=1F1F28&amp;color=C34043" alt="Open issues">
    </picture>
  </a>
</p>

<br clear="both">
<br>

## Previews

The images are rendered from the palette's terminal colors, the same values
that this theme sets.

![Terminal windows with Kanagawa Lotus, Dragon and Wave](assets/showcase.png)

<details>
<summary>🌊 Wave</summary>
<img src="assets/screenshots/wave.png" alt="Screenshot of a terminal using Kanagawa Wave">
</details>

<details>
<summary>🐉 Dragon</summary>
<img src="assets/screenshots/dragon.png" alt="Screenshot of a terminal using Kanagawa Dragon">
</details>

<details>
<summary>🪷 Lotus</summary>
<img src="assets/screenshots/lotus.png" alt="Screenshot of a terminal using Kanagawa Lotus">
</details>

## Requirements

- Windows Terminal 1.0 or later.

## Installation

Download the theme for your variant from [`themes/`](themes/), then open **Settings > Open JSON file** and add the object in the file to the `schemes` list.

## Usage

Select the scheme in a profile, for example in `profiles.defaults`:

```json
"colorScheme": "Kanagawa Wave"
```

## Palette

Every color comes from the shared
[palette](https://github.com/kanagawa-community/.github/blob/main/docs/PALETTE.md),
picked by role, so each variant uses its own value for the same role.

| Windows Terminal color                             | Palette role   |
| -------------------------------------------------- | -------------- |
| `background`                                       | `ui.bg`        |
| `foreground`                                       | `ui.fg`        |
| `cursorColor`                                      | `ui.fg_dim`    |
| `selectionBackground`                              | `ui.bg_visual` |
| `black` to `white`, `brightBlack` to `brightWhite` | `term.*`       |

## Credits

This port replaces the Windows Terminal theme in the `extras` folder of the
[Neovim plugin](https://github.com/kanagawa-community/neovim). Anton Kriese first contributed that theme to kanagawa.nvim. The
colors come from [kanagawa.nvim](https://github.com/rebelot/kanagawa.nvim) by
Tommaso Laurenzi.

## Issues and contributions

Report bugs and request changes in this port's
[issue tracker](https://github.com/kanagawa-community/windows-terminal/issues). Contributions are welcome.

See [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

MIT. See [LICENSE](LICENSE).
