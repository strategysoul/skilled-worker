# Contributing

## Add a skill

1. Pick the right plugin (`ss-product-management`, `ss-job-search`, `ss-resume`,
   `ss-ai-learning`). If none fits, add a new plugin — see below.
2. Create the directory and copy the template:

   ```bash
   mkdir -p <plugin>/skills/<skill-name>
   cp templates/SKILL.md <plugin>/skills/<skill-name>/SKILL.md
   ```

3. Write the skill. The frontmatter `name` must equal `<skill-name>`.
4. Spend real effort on the `description` — it is the only thing that makes the skill
   fire. Name the deliverable and the trigger phrases a user would type.
5. Bump the plugin's minor `version`.
6. Run the validator:

   ```bash
   python validate_plugins.py
   ```

## Add a command

Same flow with `templates/COMMAND.md`, into `<plugin>/commands/<command-name>.md`.
A command should chain existing skills by name rather than restating their content.

## Add a plugin

1. Create `<plugin>/.claude-plugin/plugin.json` (copy an existing one, change the
   fields) plus empty `skills/` and `commands/` directories.
2. Add an entry to `.claude-plugin/marketplace.json` with `name`, `description`,
   `source`, and `category`.
3. Add a row to the plugins table in `README.md`.
4. Run the validator.

## Testing a skill before committing

Ask Claude, in a fresh session, the kind of question the skill is meant to catch —
without naming the skill. If it doesn't load, the `description` is the problem, not
the body.

## Style

- Second person, imperative, concrete.
- Pin the output format.
- One framework per skill.
