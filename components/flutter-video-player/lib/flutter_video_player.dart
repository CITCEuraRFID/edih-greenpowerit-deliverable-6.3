import 'package:flutter/material.dart';
import 'package:media_kit/media_kit.dart';

/// A reusable Flutter widget that plays a video using the `media_kit` package.
///
/// This component demonstrates a minimal integration of `media_kit` for video playback.
/// It can be extended with additional features such as controls, subtitles, or
/// buffering indicators.
class VideoPlayerWidget extends StatefulWidget {
  /// URL of the video to be played.
  final String url;

  /// Whether the video should start playing automatically.
  final bool autoplay;

  const VideoPlayerWidget({
    required this.url,
    this.autoplay = false,
  });

  @override
  State<VideoPlayerWidget> createState() => _VideoPlayerWidgetState();
}

class _VideoPlayerWidgetState extends State<VideoPlayerWidget> {
  late final MediaKit _mediaKit;
  late VideoController _controller;

  @override
  void initState() {
    super.initState();
    _mediaKit = MediaKit();
    _controller = VideoController.network(widget.url)
      ..initialize().then((_) {
        if (widget.autoplay) {
          _controller.play();
        }
      });
  }

  @override
  void dispose() {
    _controller.dispose();
    _mediaKit.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: AspectRatio(
          aspectRatio: _controller.aspectRatio,
          child: VideoPlayer(_controller),
        ),
      ),
    );
  }
}