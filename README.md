# Dex++ v1.0.1

**Developed by MasterDevelopments.**
![Preview](./preview.png)

Dex++ is an extended version of Moon's Dex, made to fulfill some Moon's Dex prophecy.

## Latest Version Script
```lua
loadstring(game:HttpGet("https://github.com/finalcircuitgame-crypto/DexPlusPlus/releases/latest/download/out.lua"))()
```
For specific versions, go to [releases](https://github.com/finalcircuitgame-crypto/DexPlusPlus/releases).

## v1.0.1

- Replaced the startup Explorer's one-shot full-game descendant scan with a batched tree walk that yields every 200 indexed instances.
- Reused the incremental indexing path when large subtrees are added after startup.
- Added per-module initialization status and elapsed-time warnings to make startup stalls easier to pinpoint.
- Updated the runtime version and developer credit.

## What's the difference between Dex and Dex++?
Since the original Dex is the last release and Moon have discontinued it, it still has some missing features.
Here are the features that were added/fixed in Dex++
- Using New Roblox Studio Icons
- Updated API
- Uses Konstant, [Advanced Decompiler](https://github.com/w-a-e/Advanced-Decompiler-V3) and [Shiny](https://github.com/AZYsGithub/shiny)/[Medal](https://github.com/shrimp-nz/medal) as fallback decompilers (for shitsploits who doesn't have it)
    > 'getscriptbytecode' is required
- Uses [USSI](https://github.com/luau/UniversalSynSaveInstance/tree/main) as fallback saveinstance
- Mobile Input Support (Window drag, resizing works fully on touch)
- Console Output
- Model Viewer (basically 3D Preview)
- Revived Save Instance (original Dex doesnt have it, but does in Dex 2.0)
- Click part to select (thx Toon :3)
- CodeFrame cursor offset (where cursor on textbox were not aligned properly)

## To Build

1. Download this repository.
2. Ensure you have Python 3.9 or newer.
3. Run `python build.py` from the repository root. This generates `out.lua`.
4. Run `python build.py --check` to verify that the generated bundle matches the source files.

The builder sorts module files for reproducible output and verifies that every module listed in `Main.ModuleList` is embedded. `out.lua` is generated and intentionally ignored by Git; edit the source files instead.

### Release automation

GitHub Actions builds and verifies `out.lua` on pushes and pull requests. When a GitHub Release is published, the workflow builds `out.lua` and attaches it to that release automatically. The latest-version loader link above therefore receives the generated bundle after the release workflow completes.

## About Dex Roadmap
The concept of the Dex roadmap is amazing, however neither me nor Moon have the ability to fulfil the full roadmap. I did have added few stuffs in my fork but mostly of them are beyond my limit and i did this project for fun.

## Our Discord Server
https://discord.gg/ndhGeSGkWn

## Donation
Every donation is highly apreciated, this is compeletely optional.
- 113mGk11Hz7KoHmVhffMhFRGGt4xyofsn6 (BTC)
- 0xf66604a05c5a5372b1480a0b79f86865dccbd7db (BNB)
- 0xf66604a05c5a5372b1480a0b79f86865dccbd7db (ETH)

## Third Party Components
- Konstant Decompiler (Let me know)
- [UniversalSynapseSaveInstance (USSI)](https://github.com/luau/UniversalSynSaveInstance)
- [Advanced Decompiler](https://github.com/w-a-e/Advanced-Decompiler-V3)
- [Shiny](https://github.com/rocult/shiny)/[Medal](https://github.com/shrimp-nz/medal)

## License
[![Dex++ License](https://img.shields.io/badge/Dex++-License-green)](https://github.com/AZYsGithub/DexPlusPlus/blob/main/LICENSE)

[![USSI License](https://img.shields.io/badge/USSI-License-green)](https://github.com/luau/UniversalSynSaveInstance/blob/main/LICENSE)

## Credits
- [MasterDevelopments](https://github.com/finalcircuitgame-crypto) – Developer and maintainer of this Dex++ fork  
- [Chillz](https://github.com/AZYsGithub) – Original Dex++ maintainer and upstream project credit  
- [Cazan](https://github.com/Cazzanos) – Helped me develop the Model Viewer  
- [Moon](https://github.com/LorekeeperZinnia/Dex) – Original Dex Explorer  
- [Toon](https://github.com/Toon-arch) – Contributor and IY's Dex parts and components
