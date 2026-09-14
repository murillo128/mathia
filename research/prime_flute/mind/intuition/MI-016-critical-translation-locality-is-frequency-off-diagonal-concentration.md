# MI-016 — The seam-normalized two-pant translation test is exact, and the prime-flute tail fails it

**Evidence level:** exact necessary-condition reduction from PF-337--PF-340 and decisive tail obstruction from [PF-341](../../findings/PF-341-thin-pant-self-dtn-contrast-has-common-positive-sign.md). This kills the PF-336 normalized-insertion translation route; it does not prove the completed-angle lower bound sought by the independent direct Hilbert--Schmidt route.

PF-336 reduces completed polar translation transport to a Hilbert--Schmidt commutator of the normalized pant insertion. PF-337 diagonalizes the translation action, PF-338 compresses the finite-boundary odd sector to half-cuff cross-parity mass, and PF-339 converts the normalized condition into a raw seam-width test: every fixed odd-offset symmetric-channel coupling must be `o(w_n)`.

PF-340 identifies the exact scalar hidden by that channel. The symmetric response on cuff module `n` averages the self-DtN blocks of the two adjacent pant cores, so the explicit two-mode witness is

`Delta_n^sym = (Delta_n^-+Delta_n^+)/2`.

The translation route therefore requires `Delta_n^-+Delta_n^+=o(w_n)`. Before PF-341 this left a genuine cancellation loophole because the right-pant geometry alone could not control the left response.

PF-341 closes that loophole. For the half-cuff-exchanged pair `f_+=(c_2+c_1)/sqrt 2`, `f_-=(c_2-c_1)/sqrt 2`, the collapsing finite-finite corridor sees `f_+` with nonzero boundary value but `f_-` with a quadratic zero. On a tail pant with boundary period `L` and finite-finite separation `s`,

`<f_+,Af_+> >= c/(sL)`,

while the explicit `f_-` extension has singular cost only `O(1/(sL^5))` plus a bounded remainder. Since `sL->0`, the contrast is eventually positive. Applied on both sides of cuff `n`,

`Delta_n^+ >= c/(s_n L_n)`, `Delta_n^- >= c/(s_(n-1)L_n)`.

Thus the two adjacent terms have the **same positive sign**, and

`Delta_n^sym / w_n \gtrsim P_n^1.475/log P_n -> infinity`.

The necessary `o(w_n)` condition fails by a diverging factor on the whole tail. The normalized-insertion translation-locality architecture is therefore not merely unproved; it is falsified by the explicit lowest two-mode seam witness.

The reusable lesson is representation-specific: once a completed translation criterion is reduced to a raw local PDE response, one must test the exact bidirectional scalar produced by the cut geometry. Here that scalar survives completion but is forced large by a corridor zero/nonzero dichotomy. Returning to higher odd modes cannot repair the failed necessary condition.

**Boundary.** PF-341 does not localize a completed packet in physical space and does not rule out the independent PF-318/PF-320 direct Hilbert--Schmidt upper-bound route. Translation compatibility and direct angle control are now separate branches rather than two versions of the same endpoint.