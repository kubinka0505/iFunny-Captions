## 0.1
Alpha development.

## 0.3
Re-write.

## 0.4
Initial release.

## 2.0
### Added ➕
- GIF support. (FFmpeg >= 2.2.2)
### Fixed 📝
- Several bugs.
### Modified 🔁
- Changed fonts.

## 2.1
### Added ➕
- Font. (`Futura Bold`)
### Modified 🔁
- Several functions.
- Image creation time (FFmpeg >= 4.0.0)

## 2.2
### Added ➕
- `Logs`.
### Fixed 📝
- Several bugs.

## 2.3
### Added ➕
- `Optimization`. (`gifsicle >= 1.9.2` encoder dependency)
- Offline Support.
### Modified 🔁
- Text-wrapping system.

## 2.4
### Added ➕
- Support to following GIF services:
  - `Gfycat.com`
- Transparent GIF support. (FFmpeg >= 4.2.0)
- `Meta Info` section to `ReadMe`.
- Font randomness.
### Modified 🔁
- Renamed `Captions` to `Images`.
- The vertical distance between text-wrapped phrases.
- Replaced fonts to `OpenType` format. (`OTF`)
- Replaced examples of Images.
### Fixed 📝
- `Delay` without `Optimize` option enabled.
- Saving issues. (Forgot to replace `"` in the filename)
### Removed 🚫
- `Crop`
  - Could cause problems. (Furthermore, I don't think that anybody would use that)
- `Saving_Method`:
  - `PIL` is now used for single-framed images. (ie. `PNG`, `JPG`)
  - `FFmpeg` is now used for GIFs.

## 2.5
### Added ➕
- Support to following GIF services:
  - `ImgFlip.com`
  - `Pinterest`
- `Lossy`.
### Modified 🔁
- ReadMe structure.
- GIF Optimization structure.
- Default `Delay` value.
### Removed 🚫
- Font randomness - Created an empty file if the font was type `0` and if it returned `Roboto Black`.

## 2.6
### Added ➕
- Support to following GIF services:
  - `MakeAGif.com`
  - `Gifer.com`
  - `GifImage.net`
  - `BestAnimations.com`
  - `Gif-Finder.com`
  - `ReactionGifs.us`
  - `ReplyGIF.net`
- `Max_Width` and `Wrap_Factor` table.
- New badges.
- Dark Mode.
- HTTP Error handling.
### Modified 🔁
- `Max_Width` system.
- GIF Optimization structure.
  - `Factor` is now `3`. (in code)
  - `Factor` has been replaced to `Enabled`.
- Text-wrapping system.
- Caption Field default size.
- Image Comparisons.
- Changed Banner format from `PNG` to `SVG`.
- Configuration keys & values order.
- Delay system.
### Fixed 📝
- `Delay` without `Optimize` option enabled. **(?)**

## 2.7
### Added ➕
- Google Colab notebook.
### Modified 🔁
- Replaced `Roboto Black` to `Roboto Condensed Bold`.
- Requirements.
- `ReadMe` readability.
### Removed 🚫
- `Pinterest` support.
### Fixed 📝
- Issue where some GIFs couldn't be saved.