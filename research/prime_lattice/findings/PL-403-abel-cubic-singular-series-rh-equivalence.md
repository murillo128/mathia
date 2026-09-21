# PL-403 — Abel regularization makes the cubic singular-series zero layer an RH-equivalent asymptotic

**Evidence/status:** `EXACT-DERIVED + LITERATURE-BASED + ROUTE-ADVANCE + MODEL-LEVEL + REGULARIZATION-RESOLVED`.

**Parent findings:** `PL-401`, `PL-402`.

## Claim

`PL-402` left a precise technical obstruction: the ideal cubic kernel

\[
g(u)=\frac{\sin(\pi u^3/6)}{u}
\]

has the correct nonzero Mellin response at every zeta-zero pole of the Hardy--Littlewood pair singular series, but its vertical Mellin decay is only oscillatory, so the naive full half-line inversion is not absolutely justified. A canonical Abel damping in the **same cubic variable** resolves that obstruction without erasing the zero layer.

Fix

\[
a=\frac\pi6,\qquad \eta>0,
\]

and define

\[
w_\eta(u)
= e^{-\eta u^3}\frac{\sin(a u^3)}{u},
\qquad u>0,
\tag{1}
\]

with the continuous value `w_eta(0)=0`. Let `mathfrak S(d)` be the standard Hardy--Littlewood pair singular series used in `PL-401`--`PL-402`, and put

\[
A_\eta(H)
=\frac1H\sum_{d\ge1}\mathfrak S(d)\,w_\eta(d/H).
\tag{2}
\]

Write

\[
R_\eta=\sqrt{\eta^2+a^2},
\qquad
\phi_\eta=\arctan(a/\eta)\in(0,\pi/2).
\tag{3}
\]

Then the Mellin transform is

\[
\boxed{
\widehat w_\eta(s)
=\frac13
 \Gamma\!\left(\frac{s-1}{3}\right)
 R_\eta^{-(s-1)/3}
 \sin\!\left(\frac{\phi_\eta(s-1)}3\right),
}
\tag{4}
\]

initially by an absolutely convergent Laplace integral for `Re(s)>1` and, after the removable singularity at `s=1`, analytically throughout

\[
\Re s>-2.
\]

In particular,

\[
\widehat w_\eta(1)=\frac{\phi_\eta}{3},
\tag{5}
\]

and

\[
\widehat w_\eta(0)
=\Gamma(2/3)R_\eta^{1/3}\sin(\phi_\eta/3)>0.
\tag{6}
\]

Moreover, if `rho=beta+i gamma` is any nontrivial zero of `zeta`, and

\[
s_\rho=\frac\rho2-1,
\]

then

\[
\boxed{\widehat w_\eta(s_\rho)\ne0.}
\tag{7}
\]

For every fixed `eta>0`, the following asymptotic is therefore equivalent to RH:

\[
\boxed{
\mathrm{RH}
\iff
A_\eta(H)
=\frac{\phi_\eta}{3}
-\frac{\Gamma(2/3)R_\eta^{1/3}\sin(\phi_\eta/3)}{2H}
+O_{\eta,\varepsilon}\!\left(H^{-7/4+\varepsilon}\right)
}
\tag{8}
\]

for every `epsilon>0` as `H -> infinity`.

This is **not** a new independent RH criterion. It is a line-specific smooth consequence of the Goldston--Suriajaya continuation/Riesz theory already audited in `PL-402`. Its value is narrower and concrete: the exact cubic phase discovered in `PL-401` admits a natural Abel regulator that

1. makes Mellin inversion genuinely well behaved,
2. preserves every nontrivial-zero pole,
3. isolates the deterministic `H^-1` layer explicitly, and
4. leaves the RH-sensitive layer at exactly `H^-7/4`.

Thus the regularization issue in `PL-402` is no longer part of the live obstruction at the **singular-series model** level. The remaining hard bridge is from this model to the actual incomplete-gamma continuation statistic with an aggregate error below the same scale.

## 1. Exact Mellin transform of the cubic Abel regulator

From (1),

\[
\widehat w_\eta(s)
=\int_0^\infty
 u^{s-2}e^{-\eta u^3}\sin(a u^3)\,du.
\]

Set `t=u^3` and

\[
\nu=\frac{s-1}{3}.
\]

Then

\[
\widehat w_\eta(s)
=\frac13\int_0^\infty
 t^{\nu-1}e^{-\eta t}\sin(at)\,dt
\tag{9}
\]

and hence

\[
\widehat w_\eta(s)
=\frac{\Gamma(\nu)}{6i}
\left((\eta-ia)^{-\nu}-(\eta+ia)^{-\nu}\right).
\tag{10}
\]

Writing `eta +/- ia=R_eta e^{+/- i phi_eta}` gives (4). Although the Laplace evaluation starts with `Re(nu)>0`, the original integral behaves like `a u^{s+1}` at zero and therefore converges for `Re(s)>-2`; the apparent Gamma pole at `nu=0` is canceled by the sine factor. This gives the stated analytic continuation of the weight transform without invoking the singular-series continuation.

The special values follow directly. At `s=1`,

\[
\widehat w_\eta(1)
=\frac13\lim_{\nu\to0}
\Gamma(\nu)R_\eta^{-\nu}\sin(\phi_\eta\nu)
=\frac{\phi_\eta}{3}.
\]

At `s=0`, use `Gamma(-1/3)=-3 Gamma(2/3)` to obtain (6).

Most importantly, at `s=s_rho`,

\[
\Im\nu
=\frac{\gamma}{6}\ne0.
\]

The zeros of `sin(phi_eta nu)` are real because `phi_eta` is real and nonzero, while Gamma has no zeros. Thus (7) is exact: the Abel damping introduces no accidental zero at any nontrivial zeta-zero location.

The same formula also explains why `eta>0` is the right regularization parameter. Stirling's formula gives Gamma decay

\[
\exp(-\pi|t|/6)
\]

for `s=sigma+it`, while the sine factor grows at most like

\[
\exp(\phi_\eta|t|/3).
\]

Hence

\[
\widehat w_\eta(\sigma+it)
=\operatorname{poly}(|t|)
\exp\!\left(-\frac{\pi-2\phi_\eta}{6}|t|\right),
\tag{11}
\]

uniformly on fixed vertical strips in `Re(s)>-2`. Since `phi_eta<pi/2`, this is genuine exponential vertical decay. At the unregularized endpoint `eta=0`, `phi_eta=pi/2` and the exponential decay disappears exactly, recovering the boundary diagnosed in `PL-402`.

## 2. RH implies the `H^-7/4` remainder

Let

\[
B_m(x)=\sum_{d\le x}(x-d)^m\mathfrak S(d).
\]

Goldston--Suriajaya prove for every fixed integer `m>=2`, under RH,

\[
B_m(x)
=\frac{x^{m+1}}{m+1}
-\frac12x^m
 \left(\log x-H_m+\gamma+\log(2\pi)\right)
+O_\varepsilon(x^{m-3/4+\varepsilon}).
\tag{12}
\]

Take `m=2`. Distributionally,

\[
B_2^{(3)}(x)
=2!\sum_{d\ge1}\mathfrak S(d)\,\delta_d.
\tag{13}
\]

Pair (13) with `w_eta(x/H)` and integrate by parts three times. The first main term in (12) differentiates to the constant density `1`; the `x^2 log x` term differentiates to the density `-1/(2x)` after division by `2!`; the constant multiple of `x^2` disappears. Therefore

\[
\sum_{d\ge1}\mathfrak S(d)w_\eta(d/H)
=H\int_0^\infty w_\eta(u)\,du
-\frac12\int_0^\infty\frac{w_\eta(u)}u\,du
+O_{\eta,\varepsilon}(H^{-3/4+\varepsilon}).
\tag{14}
\]

The integrations are legitimate because `w_eta(u)=a u^2+O(u^5)` at zero and is exponentially damped at infinity. Dividing by `H` and using (5)--(6) gives the forward implication in (8).

This derivation is useful because it does not require a new estimate for `1/zeta` on a shifted contour. The hard analytic input is exactly the already-published Goldston--Suriajaya RH bound; the cubic Abel weight merely transfers it without losing the critical exponent.

## 3. The asymptotic conversely excludes every off-line zero

The reverse implication can be derived directly from Mellin uniqueness and the pole structure already established by Goldston--Suriajaya.

Let

\[
F(s)=\sum_{d\ge1}\frac{\mathfrak S(d)}{d^s},
\qquad \Re s>1.
\]

For `Re(z)<0`, absolute interchange in (2) gives

\[
\begin{aligned}
\int_0^\infty A_\eta(H)H^{z-1}\,dH
&=\sum_{d\ge1}\mathfrak S(d)
  \int_0^\infty H^{z-2}w_\eta(d/H)\,dH\\
&=F(1-z)\widehat w_\eta(1-z).
\end{aligned}
\tag{15}
\]

The small-`H` part of the left side is entire in `z`, because the Abel factor makes `A_eta(H)` exponentially small as `H -> 0`.

Assume the estimate on the right side of (8) for every `epsilon>0`, and set

\[
\mathcal R_\eta(H)
=A_\eta(H)-\widehat w_\eta(1)
+\frac{\widehat w_\eta(0)}{2H}.
\tag{16}
\]

Then

\[
T_\eta(z)=\int_1^\infty
 \mathcal R_\eta(H)H^{z-1}\,dH
\]

is analytic throughout

\[
\Re z<\frac74.
\tag{17}
\]

Indeed, for any point in that half-plane one chooses `epsilon` smaller than its distance to `7/4`.

Splitting (15) at `H=1` gives, first for `Re z<0` and then by continuation,

\[
F(1-z)\widehat w_\eta(1-z)
=E_\eta(z)+T_\eta(z)
-\frac{\widehat w_\eta(1)}{z}
-\frac{\widehat w_\eta(0)}{2(1-z)},
\tag{18}
\]

where `E_eta(z)=int_0^1 A_eta(H)H^(z-1)dH` is entire. Thus (18) continues the left side to `Re z<7/4` with no poles there except the two deterministic ones at `z=0,1`.

Goldston--Suriajaya prove that `F(s)` continues meromorphically to `Re s>-1` as

\[
F(s)
=\frac{4C_2}{2^{s+1}+1}
 \frac{\zeta(s)\zeta(s+1)}{\zeta(2s+2)}\,\mathcal G(s),
\tag{19}
\]

and that a nontrivial zero `rho` produces a pole at

\[
s_\rho=\frac\rho2-1.
\tag{20}
\]

If `beta>1/2`, then the corresponding point

\[
z_\rho=1-s_\rho=2-\frac\rho2
\]

satisfies

\[
\Re z_\rho<\frac74.
\]

Equation (7) says the weight transform is nonzero there, so the pole of `F` survives in the product on the left of (18), contradicting (17)--(18). Hence no zeta zero has real part greater than `1/2`; the functional equation then excludes real part less than `1/2` as well. This proves RH.

The converse uses no assumption of simple zeros. Multiple zeros on the critical line remain on the boundary `Re z=7/4`; logarithmic factors there are compatible with the `H^epsilon` slack in (8).

## 4. Matched control: parity has the same cubic mean but no arithmetic sublayers

The README requires a control showing that the claimed structure is not produced merely by the cubic kernel or the even-gap support. Replace the singular series by its leading parity surrogate

\[
\mathfrak S_{\rm par}(d)=2\,1_{2\mid d}.
\]

Its Dirichlet series is elementary:

\[
F_{\rm par}(s)
=2^{1-s}\zeta(s).
\tag{21}
\]

Define `A_eta^par(H)` from (2) with this replacement. Mellin inversion gives the same mean pole at `s=1`, hence the same leading cubic mass

\[
A_\eta^{\rm par}(H)=\widehat w_\eta(1)+\cdots.
\]

But (21) is analytic at `s=0` and has no denominator `zeta(2s+2)`. Because `widehat w_eta` is analytic in `Re s>-2` and has exponential vertical decay, the contour may be moved to any fixed line `Re s=-2+delta` without encountering another pole. Consequently

\[
\boxed{
A_\eta^{\rm par}(H)
=\frac{\phi_\eta}{3}
+O_{\eta,\delta}(H^{-3+\delta}).
}
\tag{22}
\]

Thus the hierarchy

\[
H^0,\qquad H^{-1},\qquad H^{-7/4+i\gamma/2}
\]

is not generated by the cubic phase alone. The parity control retains the `H^0` Gallagher mass but has neither the singular-series `H^-1` pole nor the zeta-zero layer. Those lower terms come from the rational-prime local-density Euler product in (19).

This is the precise matched-control refinement missing from the leading collapse in `PL-401`: at first order the true singular series and `2 1_(2|d)` are indistinguishable, but the first two subleading Mellin structures separate them sharply.

## 5. Abel limit recovers the ideal cubic fingerprint

The regulator is compatible with `PL-402` in the strong sense

\[
\eta\downarrow0
\quad\Longrightarrow\quad
w_\eta(u)\to g(u)
\]

pointwise for `u>0`. At the transform level,

\[
\phi_\eta\to\frac\pi2,
\qquad
R_\eta\to a,
\]

so

\[
\widehat w_\eta(1)\to\frac\pi6
\tag{23}
\]

and

\[
\widehat w_\eta(0)
\to
\frac12\left(\frac\pi6\right)^{1/3}\Gamma(2/3),
\tag{24}
\]

exactly the two ideal-kernel values computed in `PL-402`.

At every nontrivial zero location, (7) remains true for every `eta>0`, and the limiting transform is the nonzero value already proved in `PL-402`. What fails at `eta=0` is therefore **not zero sensitivity but vertical decay**. The Abel family cleanly separates those two issues.

## 6. Prior-art and novelty audit

The arithmetic input is classical and already the main source in `PL-402`:

- **D. A. Goldston, Ade Irma Suriajaya**, “A singular series average and the zeros of the Riemann zeta-function,” *Acta Arithmetica* **200** (2021), 71--90. DOI `10.4064/aa200821-24-2`, arXiv:2007.16099. Their Lemma 2.1 gives (19), Theorem 2 gives the RH bound used in (12), and their zero-pole/omega analysis establishes that the singular-series error genuinely detects off-line zeros.

Generic Mellin smoothing, Abel damping, and the implication from a power-saving asymptotic to a zero-free half-plane are standard analytic-number-theory techniques. A targeted search for the specific weight

\[
e^{-\eta u^3}\sin(\pi u^3/6)/u,
\]

its Mellin transform, and a cubic-transition singular-series RH criterion did not locate a source treating this composition. No theorem-level novelty is claimed. The stored delta is the exact line-specific bridge: the cubic continuation phase from `PL-401` has an Abel regularization whose Mellin transform is simultaneously exponentially decaying and nonvanishing at all the Goldston--Suriajaya zero poles, which turns the qualitative regularization suggestion in `PL-402` into the precise equivalence (8).

The matched parity calculation (21)--(22) is elementary but important for the line's falsification discipline: it proves that the subleading layers are arithmetic rather than a universal artifact of the chosen smoothing.

## 7. Adversarial boundaries and falsification tests

1. **Still a singular-series model.** Equation (8) is a theorem about `mathfrak S(d)`, not about the actual correlation `Lambda(r)Lambda(r+d)`. Replacing the local-density model by prime-pair data requires hard averaged correlation input and is not justified here.

2. **The Abel factor is a regulator, not new arithmetic.** It is chosen because the continuation phase is cubic and because `eta>0` supplies the missing vertical Mellin decay. The matched parity control shows that the regulator itself does not manufacture the `H^-1` or zero layers.

3. **The actual incomplete-gamma coefficient is not yet transferred at `H^-7/4`.** `PL-401` controls the aggregate continuation approximation only to order `H^-1` on fixed cubic windows. This finding removes the Mellin-regularization uncertainty but does not improve that continuation error. A genuine transfer still needs the next transition terms or a cancellation argument leaving `o(H^-7/4+epsilon)` error.

4. **The `H^-1` subtraction is mandatory.** Removing only the Gallagher mean leaves the pole at `s=0`, which is larger than the RH zero layer. Any numerical search for ordinates before subtracting this term is below the mathematically justified resolution.

5. **Nonvanishing is exact for every nontrivial zero.** A falsification would require an error in (4): since `Im((s_rho-1)/3)=gamma/6 !=0`, the sine factor cannot vanish there and Gamma has no zeros.

6. **The endpoint `eta=0` is singular in the contour argument.** One may take `eta -> 0` after deriving transform identities, but (11) degenerates at the endpoint. Claiming the same absolute contour shift directly for the unregularized kernel would reinstate the error identified in `PL-402`.

7. **The converse depends on the published pole structure of `F`.** If a correction to Goldston--Suriajaya showed that an off-line zero did not produce the stated pole of the continued pair-singular-series generating function, the reverse implication in (8) would have to be revisited. Their published continuation and residue analysis are the authority used here.

## Consequence for the line

The cubic branch now has a clean model-level spectral ladder:

\[
\text{Gallagher mean }H^0
\;\longrightarrow\;
\text{deterministic arithmetic pole }H^{-1}
\;\longrightarrow\;
\text{zeta-zero layer }H^{\rho/2-2}.
\]

The critical line is exactly the statement that the last layer begins at radial exponent `-7/4`. The Abel regulator makes this ladder rigorous while preserving the actual cubic phase and defeating the parity matched control.

Accordingly, the next useful work should **not** spend another pass on regularizing the singular-series Mellin inversion. That issue is resolved by (1)--(11). The live obstruction is the quantitative transfer left in `PL-402`: expand the continuation-faithful incomplete-gamma statistic past its `H^-1` aggregate layer and prove a remainder below `H^-7/4`, or show decisively that such a transfer cannot be made without inserting arithmetic information by hand.