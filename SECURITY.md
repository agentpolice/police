# Security

agent-police runs entirely on your machine. It does not send your code or your files anywhere.

One question goes out: when a dependency is new or upgraded, its name, ecosystem and version are sent to OSV (`api.osv.dev`) to look up known vulnerabilities (`no_known_vulns`). Nothing else is in the request. Turn it off with `"universal_off": ["no_known_vulns"]` in `harness.json`. The phone digest and the control room send a summary of what the police found (never your code), and only when you set them up.

To report a security issue, email **064105@gmail.com** with the details. Please don't open a public issue for it.
