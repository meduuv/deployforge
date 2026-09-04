# Rollback procedure

1. Confirm the failed release and affected environment.
2. Select the last known-good version.
3. Restore the previous version using the normal deployment path.
4. Run health checks and a minimal smoke test.
5. Record the cause, rollback result, and follow-up action.
