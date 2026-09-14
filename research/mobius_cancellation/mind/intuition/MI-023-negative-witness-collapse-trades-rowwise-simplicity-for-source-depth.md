# MI-023 — Blindness survives rowwise; atom-sensitive scalar decoding forces unavailable source depth

**Evidence level:** proved for the current flat Christoffel source through [MC-273](../../findings/MC-273-christoffel-negative-witness-homogeneous-collapse.md)--[MC-280](../../findings/MC-280-signed-endpoint-decoder-low-depth-parseval-barrier.md). No signed cross-row arithmetic cancellation theorem or blind-support exclusion is claimed.

MC-273--MC-277 separate representation, conditioning, normalization and aggregation. A negative witness collapses one row to a homogeneous shell, all negative witnesses can be aggregated at only one extra Walsh degree, and the normalized Christoffel scalar still retains the exact blind bit with rowwise margin `delta_(k,m)~2m/k`. The catastrophic one-exception loss appears when normalization or aggregation discards row provenance, not because the low-depth row representation has already forgotten blindness.

MC-278 first showed that replacing polynomial normalization by one rational decoder changes algebraic complexity but not the source-information bill. Its endpoint function has low rational degree, yet its nonnegative Walsh mass concentrates near degree `k/2`. MC-279 then proved a representation boundary for positive-definite pointlike decoders: positive Fourier mass cannot remain at source depth `o(k)` while the endpoint localizes onto the blind atom.

MC-280 removes positivity at the stronger accuracy demanded by the arithmetic aggregation. For an arbitrary signed or complex scalar decoder with `D(x_*)=1` and uniform off-atom error `epsilon`, the low-depth coefficient variation satisfies

`V_m(D) <= sqrt(Z_m(k)) (2^(-k)+(1-2^(-k))epsilon^2)^(1/2)`.

At the live row count, direct exceptional-row detection requires `epsilon<1/(2C)`, and with the available source depth `m=t+1` this forces `V_m(D)=o(1)`. Thus coefficient signs do not rescue a **full-cube pointwise scalar decoder** at the accuracy actually needed downstream. Almost all endpoint-producing Fourier variation must live above the available source hierarchy.

The reusable distinction is sharper than polynomial versus rational degree or positive versus signed coefficients. **Algebraic description complexity, scalar accuracy, cube domain and source-support depth are different currencies.** A concise signed scalar inverse can still demand unavailable character depth once it must suppress every nonblind row to atom-sensitive accuracy.

The surviving routes must leave that model: aggregate signed information across target rows before demanding sharp rowwise suppression, exploit restrictions of the actual localized Legendre image absent on the full Boolean cube, or act through a source-native arithmetic/operator inverse that is not represented by a uniformly sharp scalar point-selector.

**Boundary.** MC-280 does not give a universal half-depth theorem for arbitrary signed decoders at slowly vanishing error; MC-279 retains that stronger statement under positivity. It also does not constrain signed cross-row aggregation that never constructs a decoder satisfying the full-cube pointwise bound, nor a decoder defined only on the arithmetic image.