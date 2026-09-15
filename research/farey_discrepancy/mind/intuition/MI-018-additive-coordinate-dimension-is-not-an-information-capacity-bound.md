# MI-018 — Additive coordinate dimension and nominal precision are not information-capacity bounds

**Evidence level:** exact information-capacity boundary from [FD-141](../../findings/FD-141-one-infinite-precision-additive-coordinate-can-encode-the-full-squarefree-factorization.md), sharpened by [FD-142](../../findings/FD-142-log-radical-coordinate-reconstructs-the-squarefree-prefix-with-polynomial-precision.md), correcting any extrapolation of the fixed-congruence obstruction [FD-140](../../findings/FD-140-every-fixed-congruence-coordinate-alphabet-misses-a-finer-prime-color-wall.md) to arbitrary finite-dimensional or merely finite-precision strongly additive coordinates.

FD-140 proves that every fixed congruence-periodic coordinate alphabet leaves a finer coprime prime-color direction. That conclusion depends on bounded arithmetic resolution of the visible alphabet, not on finite coordinate dimension by itself.

FD-141 gives a one-dimensional exact-real counterexample: a superincreasing strongly additive coordinate is injective on the squarefree fibre. It shows that algebraic dimension can stay one while the resolving capacity grows with the entire prime alphabet.

FD-142 removes the tempting repair “require only finite or polynomial precision.” The fixed coordinate

`L(n)=sum_(p|n) log p = log rad(n)`

satisfies `L(n)=log n` on squarefree integers. For distinct squarefree `m,n<=T`, `|L(n)-L(m)|>1/T`, so the quantization `floor(2T L(n))` remains injective. It uses at most `2T log T+O(1)` symbols, hence `log_2 T+log_2 log T+O(1)` fixed-length bits. Conversely, the squarefree prefix itself has linearly many states, so every injective code already needs `Omega(log T)` bits.

Thus complete source recovery is possible with one fixed strongly additive scalar at essentially the ordinary source-identity scale `Theta(log T)` bits. The huge `Theta(pi(T))` precision cost of the superincreasing example was a property of that encoding, not a universal price for one-dimensional reconstruction.

The reusable distinction is therefore **representation size versus stable source-state capacity and provenance**. Finite dimension, finite precision and inverse-polynomial resolution all permit complete labeling. A useful ancestry condition must either keep effective capacity genuinely below the squarefree identity scale or restrict the allowed coordinates so that direct labels such as `log rad(n)` are inadmissible because they are not derived from the Farey/Franel/Fourier observable under study.

This leaves a nontrivial middle regime rather than solving it. An alphabet of size `o(T)` cannot be injective on all squarefree states, but collisions alone do not imply that a macroscopic ancestry wall survives. Likewise a source-native coordinate may carry `Theta(log T)` bits without being a literal label, and that distinction has to be proved rather than assumed. The next negative theorem needs a capacity/regularity/provenance condition strong enough to force unresolved source freedom; the next positive theorem needs to show that the retained freedom is nevertheless enough for the Farey endpoint.

**Boundary.** Both FD-141 and FD-142 are deliberately source-reconstructing controls, not positive Farey mechanisms. `L(n)=log rad(n)` is circular as an ancestry observable on the squarefree fibre because there it is simply `log n`. FD-142 does not prove that sublinear alphabet size is sufficient for coercivity, nor that `Theta(log T)` is forbidden for every source-native Farey statistic. It identifies the capacity threshold at which nominally weak one-dimensional finite-precision observation can already cease to be a meaningful compression.