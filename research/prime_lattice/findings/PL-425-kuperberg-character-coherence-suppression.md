# PL-425 — Kuperberg's mod-5 singular-series covariance is character-diagonal up to square-root error

**Evidence/status:** `LITERATURE + EXACT-DERIVED + PRIOR-ART-REDIRECT + CONDITIONAL-TRANSFER-BOUNDARY`.

**Parent findings:** `PL-415`, `PL-421`, `PL-423`, `PL-424`.

## Claim

`PL-424` isolates unsymmetrized cross-character covariance as information that scalar residue/character variances do not determine. At the **Hardy--Littlewood singular-series model level**, however, this missing coherence is already strongly constrained by existing prior art.

Vivian Kuperberg's two-term arithmetic-progression calculation implies the following specialization at modulus `5`. Let

\[
Q=\prod_{\substack{p\le h^2\\p\ne5}}p
\]

and let

\[
V_{a,b}(h):=V_2(Q,h;5,a,b),
\qquad a,b\in U_5=(\mathbb Z/5\mathbb Z)^\times,
\]

with `V_2` as in Kuperberg's equation (1.5). Then for every fixed `epsilon>0`, as `h -> infinity`,

\[
V_{a,a}(h)=D_5(h)+O_\varepsilon(h^{1/2+\varepsilon})
\tag{1}
\]

with the same `D_5(h)` for every reduced residue `a`, while for every `a\ne b`,

\[
\boxed{
V_{a,b}(h)=-\frac{h\log5}{25}
+O_\varepsilon(h^{1/2+\varepsilon}),
}
\tag{2}
\]

again independently of the ordered pair `(a,b)` at main-term level. Consequently the `4 x 4` reduced-residue matrix has the form

\[
\boxed{
V(h)=\bigl(D_5(h)-C_5(h)\bigr)I_4
+C_5(h)\mathbf1\mathbf1^*
+E(h),
\qquad
C_5(h)=-\frac{h\log5}{25},
}
\tag{3}
\]

with

\[
\|E(h)\|_{\rm op}
\ll_\varepsilon h^{1/2+\varepsilon}.
\tag{4}
\]

Let `F` be the unitary multiplicative-character table of `U_5` used in `PL-424`. Since `F^* 11^* F` is supported only on the principal-character coordinate,

\[
\boxed{
F^*V(h)F
=
\operatorname{diag}
\left(
D_5(h)+3C_5(h),
D_5(h)-C_5(h),
D_5(h)-C_5(h),
D_5(h)-C_5(h)
\right)
+\widetilde E(h),
}
\tag{5}
\]

where

\[
\|\widetilde E(h)\|_{\rm op}
\ll_\varepsilon h^{1/2+\varepsilon}.
\tag{6}
\]

Thus every **off-diagonal multiplicative-character coherence of Kuperberg's mod-5 two-term singular-series model is only square-root size**. The `PL-424` information gap therefore does not remain an unconstrained phase problem at the singular-series main-term level.

This is not an estimate for the actual von-Mangoldt covariance. The live difficulty is now sharper: one must transfer this near-character-diagonal singular-series model to the actual deterministically source-subtracted prime covariance with a matrix-valued error small enough to preserve the `PL-421` lower spectral floor. Existing one-channel variance / pair-correlation results do not automatically supply that mixed-character error theorem.

## 1. Kuperberg's one-sided residue sum

Kuperberg defines the singular series away from a fixed modulus `r` by

\[
\mathfrak S_r(H)
=
\prod_{p\nmid r}
\frac{1-\nu_H(p)/p}{(1-1/p)^{|H|}},
\tag{7}
\]

and in Lemma 3.1 studies

\[
S(r,v,h)
:=
\sum_{\substack{1\le m\le h\\m\equiv v\pmod r}}
(h-m)\mathfrak S_r(\{0,m\}).
\tag{8}
\]

For `v\ne0`, writing `d=(v,r)`, her lemma gives

\[
\begin{aligned}
S(r,v,h)
={}&\frac{h^2}{2r}
-\frac h2\frac{\varphi(r)}r
\frac{\Lambda(r/d)}{\varphi(r/d)}\\
&+\frac h{\varphi(r/d)}
\sum_{\substack{\chi\ne\chi_0\\(\bmod\ r/d)}}
\chi(v/d)L(0,\chi)L(1,\chi)A_{r,\chi}
+O_r(h^{1/2+\varepsilon}),
\end{aligned}
\tag{9}
\]

where `A_(r,chi)` is the explicit convergent Euler product in her equation (3.1). This is a theorem about restricted singular-series sums, not an assumption of the Hardy--Littlewood conjecture for actual primes.

For `r=5` and `v in U_5`, `d=1`, so

\[
S(5,v,h)
=
\frac{h^2}{10}
-\frac{h\log5}{10}
+\frac h4
\sum_{\chi\ne\chi_0\ (\bmod 5)}
\chi(v)C_\chi
+O_\varepsilon(h^{1/2+\varepsilon}),
\tag{10}
\]

with

\[
C_\chi:=L(0,\chi)L(1,\chi)A_{5,\chi}.
\tag{11}
\]

The one-sided sum can therefore carry linear-size residue dependence. The decisive simplification occurs only after passing to the symmetric difference statistic that actually enters `V_2`.

## 2. Symmetrization kills every mod-5 character-dependent linear term

Kuperberg's proof of Lemma 3.2 writes, when `a\ne b`, the two-term quantity with

\[
v\equiv a-b\pmod5
\tag{12}
\]

as

\[
V_{a,b}(h)
=
-\frac{h^2}{25}
+\frac15
\left(
S(5,v,h)+S(5,-v,h)
\right)
+O(1).
\tag{13}
\]

Insert (10). The two quadratic terms cancel `-h^2/25`, while the residue-independent linear term becomes `-h log5/25`. The character-dependent part is

\[
\frac h{20}
\sum_{\chi\ne\chi_0}
\chi(v)\bigl(1+\chi(-1)\bigr)C_\chi.
\tag{14}
\]

Hence every odd character disappears under the `v <-> -v` symmetrization. Modulo `5` there is exactly one nonprincipal even character, the quadratic character `chi_2`. For a primitive even nonprincipal Dirichlet character,

\[
L(0,\chi_2)=0;
\tag{15}
\]

in this special case it is also immediate from

\[
L(0,\chi_2)
=-\frac15\sum_{a=1}^5 a\chi_2(a)
=-\frac15(1-2-3+4)=0.
\tag{16}
\]

Therefore (14) vanishes identically, proving (2). This explains directly why Kuperberg's symmetric two-term formula cannot retain the quartic-character linear terms visible in the one-sided sum.

For `a=b`, Kuperberg's same-class formula is independent of `a` and gives

\[
D_5(h)
=
\frac h5
\sum_{\substack{d\mid Q\\d>1}}
\frac{\mu(d)^2}{\varphi(d)}
-\frac{4h}{5}\log h
+C_0(5)h,
\tag{17}
\]

up to `O_\varepsilon(h^{1/2+\varepsilon})`, with the explicit constant `C_0(5)` from her equation (3.2). Equations (2) and (17) yield the matrix decomposition (3).

## 3. The multiplicative-character basis diagonalizes the main model

The local channel in `PL-424` uses the multiplicative group `U_5`, not additive Fourier analysis on all residues modulo `5`. Nevertheless the main matrix (3) is even simpler: it is a linear combination of `I_4` and `11^*`.

The principal multiplicative character is the normalized vector `1/2 * 1`; every nonprincipal character is orthogonal to it. Therefore

\[
F^*\mathbf1\mathbf1^*F
=\operatorname{diag}(4,0,0,0),
\tag{18}
\]

and (5) follows. Since the matrix dimension is fixed,

\[
\|E(h)\|_{\rm op}
\le4\max_{a,b}|E_{a,b}(h)|,
\tag{19}
\]

which proves the square-root operator-norm error in (4)--(6).

The direct consequence for the representation-level obstruction of `PL-424` is

\[
\boxed{
(F^*V(h)F)_{\chi,\psi}
=O_\varepsilon(h^{1/2+\varepsilon})
\quad(\chi\ne\psi).
}
\tag{20}
\]

So the matched covariance controls in `PL-424` remain valid as an information-theoretic warning against variance-only reasoning, but they are much less representative of the **specific singular-series source model**: prior art already forces that model asymptotically toward a character-diagonal matrix.

## 4. What is still missing for the actual prime covariance

`PL-423` leaves the deterministic residual

\[
r_a(y;h)=P_a(y;h)-\frac h4,
\qquad a\in U_5,
\tag{21}
\]

and `PL-424` shows that its full covariance, not only its marginal variances, matters for the `PL-421` dephasing-image condition. Kuperberg's theorem controls the combinatorial singular-series model feeding the Hardy--Littlewood moment heuristic. It does **not** prove an asymptotic such as

\[
\int r_a(y;h)r_b(y;h)\,dy
=
\text{predicted singular-series main term}
+\text{small uniform error}
\tag{22}
\]

in the moving ranges required by this line.

To exploit (20), one would need a theorem whose error remains small after forming the complete `4 x 4` matrix and then taking its least eigenvalue. Equivalently in character coordinates, one needs genuine mixed estimates for

\[
\int A_\chi(y;h)\overline{A_\psi(y;h)}\,dy,
\qquad \chi\ne\psi,
\tag{23}
\]

not only separate asymptotics for

\[
\int|A_\chi(y;h)|^2\,dy.
\tag{24}
\]

The existing literature already indexed for `PL-415` illustrates the distinction. Yildirim studies Dirichlet-`L` zero pair correlation and primes in arithmetic progressions; Bui--Keating--Smith transfer between pair correlation and short-interval variances for individual Selberg-class `L`-functions; Kandhil--Languasco--Moree derive arithmetic-progression consequences from Dirichlet-`L` pair-correlation hypotheses. Those are natural diagonal-channel controls. They do not, merely by being applied character by character, imply the fixed-distinct-character mixed covariance bound (23).

Thus the current frontier is not “compute the singular-series cross coherence.” Kuperberg has already supplied enough structure to suppress it at main-term level. The live analytic problem is a **source-model replacement theorem with mixed-channel error control** strong enough for a Loewner/eigenvalue statement.

## 5. Prior-art and novelty audit

The main number-theoretic input is prior art:

- **Vivian Z. Kuperberg**, “Sums of singular series along arithmetic progressions and with smooth weights,” *International Journal of Number Theory* **21**(1) (2025), 53--74, DOI `10.1142/S1793042125500046`, arXiv `2301.06095`. Lemma 3.1 gives (9), and Lemma 3.2 / its proof gives the symmetric two-term quantity used in (13). The paper explicitly notes that the covariance model is smaller for distinct residue classes.
- **C. Yalcin Yildirim**, “The pair correlation of zeros of Dirichlet L-functions and primes in arithmetic progressions,” *Manuscripta Mathematica* **72** (1991), 325--334, DOI `10.1007/BF02568283`.
- **H. M. Bui, J. P. Keating, D. J. Smith**, “On the variance of sums of arithmetic functions over primes in short intervals and pair correlation for L-functions in the Selberg class,” *Journal of the London Mathematical Society* **94**(1) (2016), 161--185, DOI `10.1112/jlms/jdw030`, arXiv `1506.03741`.
- **Neelam Kandhil, Alessandro Languasco, Pieter Moree**, “Pair correlation of zeros of Dirichlet L-functions: a possible path towards the conjectures of Chowla, Elliott-Halberstam and Montgomery,” *Mathematische Annalen* **394** (2026), Article 43, DOI `10.1007/s00208-026-03383-y`.

No novelty is claimed for Kuperberg's restricted singular-series asymptotics, Dirichlet-character parity at `s=0`, finite Fourier diagonalization, or the variance/pair-correlation literature. The new durable value for this line is a **prior-art redirect**: the exact coherence datum isolated abstractly by `PL-424` is already suppressed in the canonical mod-5 singular-series source model, so further algebraic work on that model is unlikely to be the missing RH mechanism. What remains is the substantially stronger transfer from the model to actual prime covariances with matrix-level error control.

Targeted searches did not identify a theorem in the cited variance/pair-correlation literature that directly supplies the fixed-distinct-character mixed estimate (23) in the moving short-interval range required here. This is an absence-of-located-prior-art statement, not a novelty claim or proof that no such theorem exists.

## 6. Adversarial audit

1. **`V_2` is not the actual von-Mangoldt covariance.** It is Kuperberg's auxiliary finite singular-series/exponential-sum quantity. Calling (20) “the source model” is deliberate; promoting it to actual primes requires a separate Hardy--Littlewood/error theorem.

2. **The result does not prove the `PL-421` spectral floor.** Character diagonality controls coherence, but the dephasing-image cone also depends on the relative sizes of the principal and nonprincipal diagonal channels. Those diagonal scales and their actual-prime errors must still be controlled.

3. **The square-root error is for fixed modulus `5`.** Nothing here gives uniformity for growing `r`, growing character families, or a global prime-lattice limit.

4. **The parity cancellation uses the symmetric two-term statistic.** The one-sided quantity `S(5,v,h)` can contain linear quartic-character terms. It would be wrong to erase them before the `v` and `-v` contributions are combined as in (13).

5. **No RH, GRH, or critical-strip continuation is used.** The Kuperberg input is an unconditional singular-series calculation. The cited zero pair-correlation literature is comparison/guardrail material; hypotheses from those papers are not imported into (1)--(20).

6. **The matched-control obstruction of `PL-424` is not contradicted.** `PL-424` proves that marginal variance data alone cannot force the cone over all admissible covariance matrices. The present finding adds arithmetic structure that its controls intentionally did not assume.

## Consequence for the line

The direct continuation of the `PL-421`--`PL-424` route should no longer spend effort asking whether the Hardy--Littlewood singular-series model itself contains uncontrolled mod-5 character phases. At two-term level it does not: after the mandatory symmetric difference pairing, Kuperberg's theorem gives an `I + J` main matrix and only square-root off-diagonal character error.

The falsifiable next target is instead:

\[
\boxed{
\text{prove or disprove a mixed-character prime-covariance error bound strong enough to transfer (20) to the actual residual matrix.}
}
\tag{25}
\]

A successful bound would still have to be combined with diagonal-channel estimates to verify the `1/4` normalized spectral floor from `PL-421`. Failure would identify the precise place where the actual primes depart from the singular-series covariance model. Either outcome is materially sharper than another scalar variance calculation.
