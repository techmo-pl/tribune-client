# Tribune TTS gRPC Python client Changelog

## [1.4.0] - 2020-10-05
### Changed
- Updated the proto to version 2.0.0
### Added
- The `--output-format` option, with `pcm16` (default) and `ogg-vorbis`.

## [1.3.0] - 2020-03-30
### Changed
- Switch GRPC version to `1.24.3`.

## [1.2.1] - 2019-04-19
### Fixed
- Multithreading buffer access collision.

## [1.2.0] - 2018-12-12
### Added
- Support for setting gRPC deadline (how long the client is willing to wait for a reply from the server).

## [1.1.0] - 2018-08-28
### Added
- A possibility to use the client as a module.

## [1.0.0] - 2018-01-31
### Added
- Initial implementation.
