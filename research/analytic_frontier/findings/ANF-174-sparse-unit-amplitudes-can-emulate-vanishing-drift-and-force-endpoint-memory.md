# ANF-174 — Sparse unit amplitudes can emulate vanishing drift and force endpoint memory

**Status:** `DERIVED + SPARSE-UNIT-CONTROL + AMPLITUDE-QUANTIZATION-INSUFFICIENCY + POWER-UNIFORMITY-INSUFFICIENCY + SOURCE-PLACEMENT-GATE`. `ANF-173` showed that a tiny real carrier-aligned amplitude can accumulate bow-scale endpoint charge even when every bounded-test correlation and every fixed-order Gowers norm is small. One possible escape was that the physical residual `r_X=vartheta-Q_X` does not possess arbitrarily tunable tiny amplitudes. That escape is not available by itself. The same dangerous endpoint memory can be built with amplitudes taking only the two values `0` and `1`, with no sign tuning at all.

More precisely, in the bow regime one may place unit atoms sparsely on a coarse arithmetic grid, retain only those grid sites whose **exact** logarithmic carrier lies in one fixed angular sector, accumulate charge `asymp sqrt(X log X)` inside an initial `o(K)` segment, and then set all later amplitudes to zero. The endpoint primitive remembers the charge for `Theta(K)` prefixes, producing completion `asymp X K log X` with negligible diagonal. At the same time the support has density `1/q=o(1)`, so every bounded-test correlation on an interval of length `H` is at most `(q^{-1}+H^{-1})H`, and every fixed-order normalized Gowers norm is `O_s((q^{-1}+H^{-1})^{1/2^s})`. Choosing `q=X^gamma` gives **power-decaying** generic uniformity while preserving target-sized completion.

Thus the small-amplitude feature of `ANF-173` was not essential. Sparse occupancy can turn fixed unit atoms into an arbitrarily small effective drift. The next source theorem must use the actual **placement law of prime/rough residual mass relative to the distinguished carrier** (and possibly its joint sign/amplitude law), not merely a nonzero amplitude floor, a discrete coefficient alphabet, sparsity, fixed-log nilsequence cancellation, or fixed-order Gowers uniformity.

## 1. A sparse sector of exact carrier rays stores critical charge using only amplitudes `0` and `1`

Retain the bow regime

\[
K=X^{1-2\varepsilon+o(1)},
\qquad
0<\varepsilon<\frac1{16},
\qquad
A X^2\le U\le B X^2,
\tag{1}
\]

with fixed `0<A<B<infinity`. Fix a small constant `delta>0` and define the critical endpoint charge

\[
a_X:=\sqrt{\delta X\log X}.
\tag{2}
\]

Because `epsilon<1/16`, in particular

\[
\frac{a_X}{K}
=
X^{-1/2+2\varepsilon+o(1)}\sqrt{\delta\log X}
\longrightarrow0.
\tag{3}
\]

Choose any integer sequence `q=q_X` satisfying

\[
q\to\infty,
\qquad
q a_X=o(K).
\tag{4}
\]

Set

\[
N:=\left\lceil4\sqrt3\,a_X\right\rceil,
\qquad
j_m:=mq,
\qquad
1\le m\le N,
\tag{5}
\]

and write the exact distinguished carrier directions

\[
v_j:=(X+j)^{-iU}.
\tag{6}
\]

By (4), the last candidate site

\[
L:=Nq=o(K).
\tag{7}
\]

Partition the unit circle into six angular sectors of width `pi/3`. At least one sector contains at least `N/6` of the carrier rays `v_{j_m}`. Let `theta_X` be the center angle of such a sector and let `S` be the corresponding subset of candidate indices. Then for every `j in S`,

\[
\operatorname{Re}(e^{-i\theta_X}v_j)
\ge
\cos(\pi/6)
=
\frac{\sqrt3}{2}.
\tag{8}
\]

Define real amplitudes and endpoint coefficients by

\[
c_j:=1_S(j)\in\{0,1\},
\qquad
b_j:=c_j(X+j)^{-iU},
\qquad
1\le j<K.
\tag{9}
\]

Thus the exact carrier-ray reality constraint is satisfied in the stronger nonnegative form

\[
b_j(X+j)^{iU}=c_j\in\{0,1\}.
\tag{10}
\]

There is no continuously tunable amplitude and no sign choice. Nevertheless the charge accumulated by the end of the candidate block,

\[
Q_X:=\sum_{j\le L}b_j
=\sum_{j\in S}v_j,
\tag{11}
\]

has projection

\[
\operatorname{Re}(e^{-i\theta_X}Q_X)
\ge
\frac{\sqrt3}{2}|S|
\ge
\frac{\sqrt3}{12}N
\ge
a_X.
\tag{12}
\]

Hence

\[
\boxed{|Q_X|\ge a_X.}
\tag{13}
\]

The mechanism is therefore purely a placement mechanism: select a vanishing-density subset of sites whose exact carrier rays already point into one common sector.

## 2. The sparse unit packet produces bow-scale completion with negligible diagonal

All coefficients vanish after `L`. Consequently every prefix `r>=L` remembers the same charge:

\[
\sum_{j\le r}b_j=Q_X.
\tag{14}
\]

For the left endpoint completion used in `ANF-157`--`ANF-173`,

\[
E_-(b)
:=
\sum_{r=1}^{K-1}
\left|\sum_{j\le r}b_j\right|^2,
\tag{15}
\]

we therefore obtain from (7) and (13)

\[
E_-(b)
\ge
(K-L)|Q_X|^2
\ge
(\delta-o(1))XK\log X.
\tag{16}
\]

The endpoint diagonal remains negligible. Since `|b_j|` is the support indicator and `|S|<=N`,

\[
\Delta_-(b)
\le
K\sum_{j<K}|b_j|^2
=K|S|
\le KN
\ll K\sqrt{X\log X}
=o(XK\log X).
\tag{17}
\]

Thus the target-sized completion in (16) is genuinely off-diagonal rather than a large coefficient-energy artifact. The dyadic ledger of `ANF-169` then forces at least one lag shell with positive real correlation of target order, and the exact positive representation of `ANF-172` converts the same statement into a Fejer scale-slope defect:

\[
\boxed{
D_{2H}-D_H
\gg_\delta
\frac{X\log X}{\log K}
}
\tag{18}
\]

for some dyadic `H`, up to the fixed absolute constants already recorded there.

So amplitude quantization does not protect the exact downstream decision statistic. A control with the smallest possible nonzero amplitude equal to one still produces the forbidden scale-slope anomaly.

## 3. Sparse placement simultaneously gives power-small bounded-test and fixed-order Gowers uniformity

The support `S` is a subset of the arithmetic grid `q Z`. Therefore every contiguous interval `I` of coefficient indices, of length `H`, satisfies

\[
|S\cap I|
\le
\frac Hq+1.
\tag{19}
\]

Let `F` be **any** complex test sequence with `|F(j)|<=1`. From (9) and (19),

\[
\left|
\sum_{j\in I}b_jF(j)
\right|
\le
|S\cap I|
\le
\frac Hq+1
=
H\left(q^{-1}+H^{-1}\right).
\tag{20}
\]

This bound is independent of the structure of `F`; it applies even if the test is chosen after seeing the sparse packet. Hence on all intervals `H>=H_0`,

\[
\boxed{
\sup_{|F|\le1}
\frac1H
\left|
\sum_{j\in I}b_jF(j)
\right|
\le
q^{-1}+H_0^{-1}.
}
\tag{21}
\]

The same support count controls every fixed-order normalized Gowers norm. For fixed `s>=2`, take the standard short-interval cube definition used in the higher-uniformity inputs of `ANF-165` and `ANF-173`. In the `2^s`-th power of the norm, a nonzero cube must in particular have its zero corner at a support site. For each such zero corner there are only `O_s(H^s)` admissible step tuples, while the normalization has size `asymp_s H^(s+1)`. Thus

\[
\|b\|_{U^s(I)}^{2^s}
\ll_s
\frac{|S\cap I|}{H}
\ll
q^{-1}+H^{-1},
\tag{22}
\]

and therefore

\[
\boxed{
\|b\|_{U^s(I)}
\ll_s
\left(q^{-1}+H^{-1}\right)^{1/2^s}.
}
\tag{23}
\]

This is weaker in exponent than the amplitude-small bound in `ANF-173`, but it is still power-small for every fixed order when `q` is a power of `X`.

Indeed choose any fixed

\[
0<\gamma<\frac12-2\varepsilon
\tag{24}
\]

and take `q=floor(X^gamma)` after an immaterial adjustment to keep `q>=2`. Then (4) holds because

\[
q a_X
=
X^{1/2+\gamma+o(1)}\sqrt{\log X}
=o(K),
\tag{25}
\]

while on the all-interval activation range of `ANF-173`, say `H>=X^(5/8+eta)`, equations (21) and (23) give

\[
\sup_{|F|\le1}
H^{-1}\left|\sum_{j\in I}b_jF(j)\right|
\ll
X^{-\gamma}+X^{-5/8-\eta},
\tag{26}
\]

and, for every fixed `s`,

\[
\|b\|_{U^s(I)}
\ll_s
\left(X^{-\gamma}+X^{-5/8-\eta}\right)^{1/2^s}.
\tag{27}
\]

Both decay by a fixed power of `X`, hence faster than every fixed negative power of `log X`. Nevertheless (16) and (18) still hold. Thus the obstruction is not an artifact of permitting a small continuous coefficient at every site: sparse unit occupancy reproduces the same effective drift while satisfying much stronger generic relative-uniformity statements.

## 4. What information is still absent from the matched control

The construction deliberately uses a freedom that the physical residual does not possess: it chooses **where** the nonzero unit atoms occur after looking at the exact carrier phase. The amplitudes themselves are maximally rigid. They are nonnegative and belong to the fixed alphabet `{0,1}`; the support has vanishing density and may even be placed on a deterministic coarse grid. What remains adversarial is the selection of the occupied grid sites according to their carrier sector.

Therefore `ANF-173`'s phrase "source amplitude and placement law" can now be sharpened. A lower bound on nonzero amplitude, integrality, a finite alphabet, or sparsity alone cannot close the endpoint gate. The proof must constrain the **joint placement of prime/rough residual mass relative to the logarithmic phase** strongly enough to prevent a sector-selected charge of size `sqrt(X log X)` from being stored before the endpoint horizon ends.

One source-faithful target is still the signed shell of `ANF-169`, equivalently the coupled Fejer scale slope of `ANF-172`. Another formulation suggested by the present control is an absolute discrepancy estimate for the actual residual against carrier-sector selectors: if a dangerous charge exists, some angular projection necessarily sees excess source mass on sites where the carrier points into a favorable sector. Such an estimate has to operate at the absolute `sqrt(X log X)` charging scale, not merely at relative `o(1)` precision.

This does **not** prove that primes or rough numbers realize the sparse packet. It proves the opposite kind of statement: any future closure argument that uses only generic coefficient quantization/sparsity plus relative pseudorandomness still admits a matched control with the forbidden endpoint behavior. The remaining gate is genuinely a source-placement theorem.

## 5. Relation to the current frontier and prior-art audit

`ANF-168` showed that keeping the exact logarithmic carrier and real amplitudes does not control endpoint memory. `ANF-173` strengthened this by making all amplitudes uniformly tiny, so every bounded-test correlation and every fixed-order Gowers norm is tiny even though the primitive stores critical charge. The present finding removes the apparent dependence on tiny tunable amplitudes: a sparse subset of fixed unit atoms gives the same endpoint obstruction, while its density alone makes generic bounded-test and fixed-order Gowers statistics power-small on long intervals.

The higher-uniformity literature used in `ANF-173` remains consistent with this boundary: those theorems supply relative pseudorandomness of arithmetic residuals on long intervals, whereas the present matched control shows that such information, even strengthened to every bounded test and power decay, does not by itself constrain sparse carrier-adapted occupancy at the absolute endpoint-memory scale. The construction and estimates (5)--(27) are elementary and internal; no external theorem is load-bearing here, so no new source entry is required.

## Verdict

The small-amplitude mechanism of `ANF-173` was not the essential obstruction. **Sparse placement can emulate a vanishing coherent drift with amplitudes restricted to `{0,1}`.** In the difficult bow range there are controls with exact logarithmic carrier, nonnegative unit amplitudes, vanishing support density, power-small correlations against every bounded test on all long intervals, and power-small fixed-order Gowers norms, yet with

\[
E_-(b)\asymp XK\log X
\]

and a target-sized positive Fejer scale-slope defect.

The analytic frontier therefore moves from a generic "amplitude/placement" gate to a sharper **source-placement gate**: the next theorem must exploit where the actual prime/rough residual mass occurs relative to the distinguished carrier, or directly prove the corresponding signed dyadic/Fejer defect is absolutely small. Coefficient discreteness, amplitude floors, sparsity, stronger fixed-log cancellation, and fixed-order higher uniformity are not sufficient substitutes.