## 0.1
Alpha development.

## 0.3
Re-write.

## 0.4
Initial release.

## 2.0
Bug-fixing.
Added GIF support. (ffmpeg >= 2.2.2)
Changed fonts.

## 2.1
Modified several functions.
Optimized creation time (ffmpeg >= 4.0.0)
Added font.

## 2.2
Bug-fixing.
Added `Logs`.

## 2.3
Added `gifsicle >= 1.9.2` encoder dependency.
Added `Optimization`.
Added Offline Support.
Modified text-wrapping system.

## 2.4
Updated fonts to `OpenType` format (`otf`).
Increased vertical distance between text-wrapped phrases.
Fixed `Delay` without `Optimize` option enabled.
Fixed saving issues. (Forgot to replace `"` in file name)
Added Gfycat support.
Removed `Crop`.
Removed `Saving_Method`:
- `PIL` is now used for single-framed images. (i.e. `PNG`, `JPG`)
- `ffmpeg` is now used for GIFs.

Added transparent GIF support. (ffmpeg >= 4.2.0)