Before implementing a new feature or making significant changes to existing code, please follow these steps:
1. **Check Implementation Status**: Review `docs/IMPLEMENTATION_PLAN.md` FIRST to understand current project state, what's completed, what's in progress, and what's blocked. Update this document after completing work.
2. Review the overview.md and project_plan.md files for additional context about the project and its goals, and to decide the project struture and abide by its guidelines.
2. **Understand the Requirements**: Clearly define what the feature or change is supposed to accomplish. Gather all necessary information and clarify any ambiguities.
3. **Research**: Look into existing solutions, libraries, or frameworks that might help in implementing the feature. Check for best practices and potential pitfalls.
4. **Plan the Implementation**: Outline the steps needed to implement the feature. 
5. **Write Tests**: Before coding, write tests that will validate the functionality of the new feature or change. If tests already exist, review and update them as necessary.
6. **Use project's virtual environment**: When running anything in terminal, make sure .venv is activated for the project
7. **Avoid code duplication**: reuse existing functions and modules wherever possible.

After implementing the feature or change, follow these steps:
1.  Refactor code to improve readability and maintainability, adhering to the project's coding standards and best practices.
2. Ensure to run all relevant tests to verify that everything works as expected and that no existing functionality is broken.
3. Assume you are a QA engineer and think about edge cases and potential issues that might arise from the new feature or change. Write additional tests if necessary to cover these scenarios. Document any concerns and assumptions
4. Update any documentation files to reflect the new feature or change. This includes code comments, README files, and any other relevant documentation.
5. **Update IMPLEMENTATION_PLAN_V3.md**: Mark completed tasks, add session notes in the "Session Handoff Notes" section, and update blockers if applicable in the file that is being referenced.

## Skill Routing
Before responding to any prompt, check `.github/skills/using-superpowers` for routing rules to determine which skill(s) to apply.