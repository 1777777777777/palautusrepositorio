Up to this point, I've always used OpenCode as a dedicated program. I was actually quite impressed with it. The UI and UX felt really clean and easy to use, compared to many other harnesses. The CLI version is horrible though. It feels worse to use than eg. the CLI versions of Codex and Claude Code.

Ppasting, for some reason is, implemented weirdly. I had to Google to figure out how to paste. I do not like it.

Also, I'm not really sure about the two-step approach to agentic coding. I know that harnesses are somewhat important still, but I'm skeptical about creating explicit planning and building stages. This is usually done by the models themselves nowadays.

Personally, for my projects, I rarely if ever use manual approval for code changes. At that point, it is marginally faster than me writing the code myself. Of course, this one exercise is not really a good example of it, since the AI agent was tasked with writing a single method.

But even then, if you give it a larger workload, it does not make sense to then sit there for a while approving its changes. It is also overly optimistic to assume that a person would actually bother reading those code changes in the first place. Maybe the first few. A fully agentic approach is much more honest in this regard.

The `top_goal_scorers` method did not look like the rest of the code, I feel. It used `lambda` and list slicing instead of a helper function and loop like the rest of the class. The code itself worked.

The explanations of the Pylint errors were also correct. The agent did not find any actual issues with the code. Pylint passed without errors.

The agent created unit tests using a `PlayerReaderStub` without network calls. `Player` objects are initialized with a dictionary here though.

For context, I used GPT-5 mini and GPT 6.1 Sol.