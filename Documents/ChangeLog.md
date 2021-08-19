# `ChangeLog.md` 📝

Legend:

♾️ - Google Colab notebook changes.

---

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
- Decreased image creation time (FFmpeg >= 4.0.0)

## 2.2
### Added ➕
- `Logs`.
### Fixed 📝
- Several bugs.

## 2.3
### Added ➕
- `Optimization`. (`Gifsicle >= 1.9.2` encoder dependency)
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
- Replaced examples in `Images`.
### Fixed 📝
- `Delay` without `Optimize` option enabled.
- Saving issues.
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
- `ReadMe` structure.
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
  - `Factor` has been replaced with `Enabled`.
- Text-wrapping system.
- Caption Field default size.
- Image Comparisons.
- Changed Banner format from `PNG` to `SVG`.
- Configuration keys & values order.
- Delay system.

## 2.7
### Added ➕
- Google Colab notebook. ♾️
### Modified 🔁
- Replaced `Roboto Black` with `Roboto Condensed Bold`.
- Requirements.
- `ReadMe` readability.
### Removed 🚫
- `Pinterest` support. (*although still in code*)
### Fixed 📝
- Some GIFs couldn't be saved.

## 2.8
### Added ➕
- Emoji support. 🥳
- `requirements.txt`
- Issues Templates.
- Automatic text-wrap.
- Utility scripts.
- Wiki.
### Modified 🔁
- Replaced `Futura Extra Black Condensed Regular` to `Futura Condensed Extra Bold`.
  - A lot more characters are supported now.
- Requirements.
- Replaced examples in `Images`.
- Renamed `Logs` to `Time_Logs`
- Program files structure.
- `Dark_Mode` font color to `#A0A0A0`.
- Increased Font quality.
- File detection system.
### Removed 🚫
- `Wrap_Factor`.
- `Max_Width`.
- [ReplyGIF.net](https://replygif.net) support.
- Google Colab notebook. ♾️

## Re-release 2.8
### Added ➕
- Google Colab notebook. ♾️
- `Folders` Wiki page.
### Modified 🔁
- Replaced examples in `Images`.
### Fixed 📝
- `ReadMe` URLs.

## 2.9
### Added ➕
- `auepa` API support.
- Frames extraction interruption.
- Empty captions support.
- Increased control of text height spacing.
- Metadata system.
- Cache system.
- `Run.bat` - for Windows users.
- `Kerning`.
- `Colored_Prints`.
- `Sound`.
- `emojicdn` API style selection.
### Modified 🔁
- Notebook prints. ♾️
- Relicensed program to GPL V3.
- Replaced banner with the old one, but with `SVG` format.
- Changed files extension from `py` to `pyw`.
### Fixed 📝
- Saving one-framed images to GIF instead of PNG. ♾️
- Font type. ♾️
- Capitalized acute accent letters rendering.
- Lower diactric hooks letters rendering.
- `auepa` emoji rendering.
- Emojis rendering.
- Font randomness.

## Re-release 2.9
### Added ➕
- Newline support.
- `Documents/iFunny-Captions.svg`
### Modified 🔁
- Notebook banner. ♾️
- Switched to percentage calculation system.
### Fixed 📝
- Some notebook bugs. ♾️
### Removed 🚫
- `Documents/CONTRIBUTING.md`

## 3.0
### Added ➕
- `.gitignore`
- `FFmpeg Locations` exception handling.
- Support for media streams.
### Fixed 📝
- Non-URL files import.
- Cache system.

## 3.1
### Added ➕
- More user interaction.
### Modified 🔁
- `Colored_Prints` Values.
- Program files structure.
- Cache folder.
- Removed spaces from `Config.json` keys.
- `Percentage_Elements_Size` default values.
- Requirements.
### Fixed 📝
- Several bugs.
### Removed 🚫
- `.gitignore`
- Some Utility scripts.