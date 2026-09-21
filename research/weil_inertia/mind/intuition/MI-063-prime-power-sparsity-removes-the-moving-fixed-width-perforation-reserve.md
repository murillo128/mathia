# MI-063 — Prime-power sparsity removes the moving fixed-width perforation reserve

**Evidence level:** exact/asymptotic source-transfer synthesis from [WI-384](../../findings/WI-384-prime-power-source-sparsity-removes-the-fixed-scale-perforation-uncertainty.md), sharpening the `O_L(1)` uncertainty left by WI-382--WI-383.

The fixed-width source holes are not arbitrary integer perforations. They are generated only by prime-power slots. In the centered window relevant to the WI-380 trial family, the number of such slots is smaller by a logarithmic factor, giving total perforation measure

`O_L(1/(sqrt(x_k) log x_k))`.

That improvement propagates through the positive lobe and its autocorrelation: the source-dependent kernel perturbation is `O_L(1/(sqrt(x_k) log x_k))`. Since the critical arithmetic sum has total `Lambda(n)/sqrt(n)` mass `O_L(sqrt(x_k))` on a fixed logarithmic annulus, the moving source-dependent contribution is only `O_L(1/log x_k)=o(1)`.

Consequently WI-384 upgrades the exact arithmetic-plus-polar layer from an unknown bounded correction to

`Q_k^arith + Q_k^pol = R_L(x_k) - 2 R_L(1) + O_L(1/log x_k)`.

The formerly possible `k`-dependent order-one repair reserve therefore does not exist in this fixed-width family. Source perforation leaves one explicit stationary scalar, `-2R_L(1)`, plus a vanishing error. Under failure of RH the layer still has liminf `-infinity`; under RH its floor is the concrete scalar `-A_L-2R_L(1)`.

The direct-repair question is therefore no longer “can the hidden `O(1)` perforation term have the right sign?” Any surviving fixed-width repair has to come from the exact stationary balance with the archimedean block, an admissible-domain restriction, or another source coupling not represented by the moving perforation error.

**Boundary.** WI-384 does not by itself determine the sign of `-A_L-2R_L(1)` and does not include the final archimedean energy. The conclusion is specific to the certified fixed-width source-zero family and its prime-power slot geometry; it is not a general statement that all source perforations are negligible.