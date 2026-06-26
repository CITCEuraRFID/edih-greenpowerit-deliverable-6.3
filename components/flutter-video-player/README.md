# flutter_video_player

## Purpose
A reusable Flutter component that wraps the `media_kit` package to provide easy video playback functionality.

## Technologies
Flutter, media_kit

## Installation
1. Add the component directory to your project's `pubspec.yaml` or copy the `lib/` folder into your component library.
2. Run `flutter pub get` to fetch dependencies.

## Usage
```dart
import 'package:flutter_video_player/flutter_video_player.dart';

final player = VideoPlayerWidget(
  url: 'https://example.com/sample_video.mp4',
  autoplay: true,
);
```

See the [official documentation](https://pub.dev/packages/media_kit) for a full demonstration.