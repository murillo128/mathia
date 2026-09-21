# MI-047 — The first surviving Wang tail moment always pays the phase-entropy gate

**Evidence level:** exact synthesis from [VIS-348](../../findings/VIS-348-higher-wang-moments-inherit-phase-entropy-gate.md), extending the first-moment concentration bounds VIS-346--VIS-347 through Wang's exact higher tail and exact lower-order moment cancellation. The Turán--Nazarov ingredient is classical.

For a finite translated-dilate Wang bank, let `P_(q,X)` be the exponential polynomial formed by the `q`th inverse-scale moments in each translation fiber. Suppose the lower moment polynomials vanish identically,

`P_(1,X)=...=P_(q-1,X)=0`,

and the bank claims one additional local inverse-frequency order on a window `J_X subset [X,2X]`. VIS-348 shows that the first surviving moment must satisfy

`sup_(J_X)|P_(q,X)| <= D_(q,X)/X`,

where `D_(q,X)` keeps the next-order coefficient/dilation budget explicit.

Once isolated in this way, `P_(q,X)` is again a finite exponential polynomial. If it has `B_(q,X)>=2` active phases, minimum gap `Delta_(q,X)`, window length `ell_X`, and moment vector `S_(q,X)`, the same Turán--Nazarov concentration ledger reappears:

`(B_(q,X)-1) log(A L_(q,X)/e_(q,X)) >= log(X ||S_(q,X)||_2/(sqrt(2) D_(q,X)))`.

Under nondegenerate conditioning, fixed `B` and power-law window/gap scales still require `(B-1)(alpha+beta)>=1`, while macroscopic uniformly separated phases require `B log B` of order at least `log X`. The threshold does not get cheaper because several lower tail orders were cancelled exactly.

Thus **exact low-order moment cancellation and local concentration are separate resources**. A finite-bank proposal must expose the entire moment ledger: exact zeros up to the first surviving order, then the phase count, spacing and conditioning that pay to hide that surviving coefficient on the target window.

**Boundary.** The theorem conditions on exact cancellation of all lower moment polynomials. It does not classify cancellation caused by interactions among several simultaneously nonzero asymptotic orders, frequency/source-dependent coefficients, infinite expansions, or signed arithmetic cancellation in the theta remainder itself.