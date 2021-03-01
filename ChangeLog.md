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
- Modified several functions.
- Image creation time (FFmpeg >= 4.0.0)

## 2.2
### Added ➕
- `Logs`.
### Fixed 📝
- Several bugs.

## 2.3
### Added ➕
- `gifsicle >= 1.9.2` encoder dependency.
- `Optimization`.
- Offline Support.
### Modified 🔁
- Text-wrapping system.

## 2.4
### Added ➕
- Gfycat support.
- Transparent GIF support. (FFmpeg >= 4.2.0)
- `Meta` section to `ReadMe`.
- Font randomness.
###Modified 🔁
- Renamed `Captions` to `Images`.
- Modified the vertical distance between text-wrapped phrases.
- Replaced fonts to `OpenType` format. (`otf`)
- Replaced examples Images.
### Fixed 📝
- `Delay` without `Optimize` option enabled.
- Saving issues. (Forgot to replace `"` in the filename)
### Removed 🚫
- `Crop`
  - Could cause problems. Furthermore I don't think that anybody would use it.
- `Saving_Method`:
  - `PIL` is now used for single-framed images. (ie. `PNG`, `JPG`)
  - `FFmpeg` is now used for GIFs.