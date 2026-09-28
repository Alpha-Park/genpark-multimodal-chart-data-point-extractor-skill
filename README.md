# genpark-chart-coordinates

Calibrate linear chart axes and convert supplied bar or scatter pixel coordinates to values. No image recognition or logarithmic axes.

Python 3.9+; standard library runtime; MIT license.

## Install and run

Download `genpark-chart-coordinates.mcpb` from [GitHub Releases](https://github.com/Alpha-Park/genpark-multimodal-chart-data-point-extractor-skill/releases/tag/v1.0.1) and install with an MCPB-compatible client. Python must be installed and available as `python`.

Alternatively clone this repository and configure an MCP stdio server with command `python` and arguments containing the absolute path to `mcp_server.py`.

[Smithery listing](https://smithery.ai/servers/krispang1020/genpark-chart-coordinates)

## Tools

- `calibrate_axis_scale`
- `extract_bar_chart_series`
- `extract_scatter_points`
- `run_benchmark_chart_extraction`

Run `python -m unittest discover -s tests` for regression checks. The official MCP SDK integration check uses the development dependency `mcp`: `python tests/check_mcp.py`.

## Limitations

These are deterministic helpers operating on supplied structured data, not machine-learning models. Input and output remain in the local process. No hosted endpoint, automatic file access or network access is required. State lasts only for the current process. Benchmark tools run synthetic examples in isolated state; their status is not a production-quality certification.

Bar outputs are axis values at their tops, not differences from the baseline. Supply slope/intercept calibration results; linear axes only.
