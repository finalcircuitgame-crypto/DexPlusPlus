# Changelog

## v1.0.1

- Changed the displayed developer credit to MasterDevelopments.
- Set the runtime and bundled-script version to 1.0.1.
- Pointed remote module updates at the finalcircuitgame-crypto/DexPlusPlus fork.
- Corrected the remote module directory casing to match the repository's modules/ path.
- Reworked Explorer startup indexing to walk the instance tree in batches and yield every 200 indexed instances.
- Reused the batched indexing path for newly added subtrees, avoiding another unbounded GetDescendants scan.
- Added per-app initialization progress and elapsed-time warnings to make any remaining startup bottleneck identifiable.

## Previous versions

See the Git history for changes before v1.0.1.
