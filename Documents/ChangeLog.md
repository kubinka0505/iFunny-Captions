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
- `Optimization`. (`Gifsicle` >= 1.9.2`)
- Paths support.
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
- `Saving_Method`:
  - `PIL` is now used for static images. (i.e. `PNG`, `JPG`)
  - `FFmpeg` for dynamic.

## 2.5
### Added ➕
- Support to following GIF services:
  - `ImgFlip.com`
  - `Pinterest`
- `Lossy`.
### Modified 🔁
- `ReadMe` structure.
- GIF Optimization.
- Default `Delay` value.
### Removed 🚫
- Font randomness.

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
- `Dark_Mode`.
- URL Error handling.
### Modified 🔁
- `Max_Width` system.
- GIF Optimization.
  - `Factor` is now `3`. (in code)
  - `Factor` has been replaced with `Enabled`.
- Text-wrapping system.
- Caption Field default size.
- Image comparisons.
- Configuration keys & values order.
- `Delay` system.

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
- Re-licensed program to GPL V3.
- Replaced banner with the old one, but with `SVG` format.
- Changed files extension from `py` to `pyw`.
### Fixed 📝
- Saving static images to GIF instead of PNG. ♾️
- Font type. ♾️
- Capitalized acute accent letters rendering.
- Lower diacritic hooks letters rendering.
- `auepa` emoji rendering.
- Emojis rendering.
- Font randomness.

## Re-release 2.9
### Added ➕
- Newline support.
- `Documents/iFunny-Captions.svg`
### Modified 🔁
- Notebook banner. ♾️
- Caption size calculation system.
### Fixed 📝
- Some notebook bugs. ♾️
### Removed 🚫
- `Documents/CONTRIBUTING.md`

## 3.0
### Added ➕
- `.gitignore`
- `FFmpeg` location exception handling.
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

## 3.2
### Added ➕
- Linux (Ubuntu) support.
- More selectable files formats.
- Manual CLI handling for empty string values:
  - Text
  - Image
### Fixed 📝
- Fonts sorting bug.

## Re-release 3.2
### Added ➕
- More CLI messages.
- Program showcase.
### Fixed 📝
- Frames copying interruption.
- Frames extraction interruption.

## 3.3
### Added ➕
- Further optimization for grayscale images.
- More Command Line Interface arguments.
- Customizable `Colored_Prints` colors.
- `Scale_Back`.
### Fixed 📝
- Several bugs.
- `Open_Folder`.
- Google Colab Notebook. ♾️

## 3.4
### Added ➕
- More Command Line Interface arguments.
- Customizable caption colors.
- Support for captions with given audio as `MP4` videos.
- `Watermark` option.
### Fixed 📝
- Default `Dark_Mode`.
- First frame of transparent dynamic images overlapping. (FFmpeg >= 4.3.2)
- Grainy static images rendering.
- Grayscale optimization.
- Static images optimization.
- Increased documentation readability.
### Modified 🔁
- Packages locating system.
- Popup is not hidden at default.
- Character rendering system.
- Metadata system.
### Removed 🚫
- `Emoji_Height_Spacing`

## 3.5
### Added ➕
- `Side → Mono` audio channel mode.
- Exception handling for unopenable audio files.
- Automatic detections systems for:
  - Delay
  - Audio Bitrate
- Audio metadata.
- Improved quality for static images captions.
- Updates notification system.
- Command Line Interface support for several values in `Config.json` keys.
- More Command Line Interface arguments.
### Modified 🔁
- `Tenor` GIF image service.
- Metadata addition system.
- Removal of multiple underscores in filenames.
### Fixed 📝
- Feature Request addition template.
- Saving media with dots.
- Default colored prints values.
- Google Colab Notebook. ♾️

## 3.6
### Added ➕
- `OxiPNG` support.
- [User-Agent](https://wikipedia.org/wiki/User_agent).
### Fixed 📝
- Several bugs.
- Batch files shortcuts.
- Google Colab Notebook. ♾️
- Status codes for `Utility/Get_Caption_Data.pyw`.
- `Reddit` *preview* image service.
- Output filepath information.
### Modified 🔁
- Metadata addition system.
### Fixed 📝
- Argument parser audio local filepath recognition.
### Removed 🚫
- Automatic audio codec detection.