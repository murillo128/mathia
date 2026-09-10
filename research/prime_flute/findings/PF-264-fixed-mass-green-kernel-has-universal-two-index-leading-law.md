# PF-264 — fixed-mass Green kernel has a universal two-index leading law

**Status:** `LITERATURE+DERIVED + TWO-INDEX-GREEN-ASYMPTOTIC + CONNECTION-COEFFICIENT-CANCELLATION + FINITE-SEAM-ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-262-massive-jacobi-resolvents-have-exact-double-root-indicial-law|PF-262]] identifies the two indicial powers of each fixed-mass parity recurrence, and [[research/prime_flute/findings/PF-263-resonant-mass-green-tail-keeps-the-pure-recessive-power|PF-263]] shows that the recessive power survives unchanged at the integer-difference masses. Combining those asymptotics with the exact discrete Wronskian formula removes one more apparent free parameter: when **both** Green indices tend into the tail at fixed mass, the unknown connection coefficient cancels between the left regular solution and the Wronskian.

For every fixed `a>0`, parity `\varepsilon\in\{0,1\}`, and indices `i\le j` tending to infinity,

\[
\boxed{
\langle e_{2i+\varepsilon},(L+a^2)^{-1}e_{2j+\varepsilon}\rangle
=
\frac{1}{2\mu}\,
i^{-1/2+\mu}
j^{-1/2-\mu}
\left(1+O_a(i^{-1})+O_a(j^{-1})\right),
\qquad
\mu=\sqrt{1+a^2}.
}
\tag{1}
\]

The leading coefficient `1/(2\mu)` is universal: it is independent of the parity block and of the left boundary connection coefficient. At resonant masses the dominant solution may contain the subordinate logarithmic term from PF-263, but that term is lower order and does not change (1).

This gives the first canonical **moving-source** Green law for the PF-261 massive-resolvent route. It does not yet solve the finite-seam problem because the error terms are only fixed-`a`; nevertheless, it shows exactly what a successful parameter-uniform theorem must stabilize rather than leaving the source-index dependence as an arbitrary connection coefficient.

## 1. Tail fundamental system

Work in one PF-262 parity block and write its homogeneous recurrence as

\[
p_{n-1}u_{n-1}+q_nu_n+p_nu_{n+1}=0.
\tag{2}
\]

PF-262 proves

\[
p_n=-n^2-c_\varepsilon n+O(1),
\tag{3}
\]

and the coincident-root indicial exponents

\[
\rho_+=-\frac12+\mu,
\qquad
\rho_-=-\frac12-\mu,
\qquad
\mu=\sqrt{1+a^2}>1.
\tag{4}
\]

For nonresonant fixed mass, DLMF §2.9(ii) gives a fundamental pair normalized by

\[
u_+(n)=n^{\rho_+}\left(1+O_a(n^{-1})\right),
\qquad
u_-(n)=n^{\rho_-}\left(1+O_a(n^{-1})\right).
\tag{5}
\]

For a resonant fixed mass, PF-263 applies the integer-difference clause of the same theorem: `u_-` still has the second asymptotic in (5), while an independent dominant solution may be chosen with

\[
u_+(n)=n^{\rho_+}\left(1+O_a(n^{-1})\right)
+c(a)u_-(n)\log n.
\tag{6}
\]

Because `\rho_+-\rho_-=2\mu>2`, the logarithmic term in (6) is `o(n^{\rho_+-1})`; hence it is absorbed by the displayed relative `O_a(n^{-1})` precision whenever only the dominant leading law is used.

## 2. The discrete Wronskian fixes the normalization

For two solutions of (2), use the Jacobi Wronskian

\[
W_n(u,v)
:=p_n\bigl(u_n v_{n+1}-u_{n+1}v_n\bigr).
\tag{7}
\]

Green's identity makes `W_n` independent of `n`. Substituting the normalized asymptotics (3)--(5) gives

\[
\begin{aligned}
W_n(u_+,u_-)
&=p_n n^{\rho_++\rho_-}
\left[
\left(1+\frac1n\right)^{\rho_-}
-
\left(1+\frac1n\right)^{\rho_+}
+O_a(n^{-2})
\right] \\
&=\bigl(-n^2+O(n)\bigr)n^{-1}
\left[-\frac{2\mu}{n}+O_a(n^{-2})\right] \\
&=2\mu+O_a(n^{-1}).
\end{aligned}
\tag{8}
\]

Since the Wronskian is exactly constant,

\[
\boxed{W(u_+,u_-)=2\mu.}
\tag{9}
\]

The same calculation is valid at resonance because the logarithmic correction in (6) is a multiple of `u_-` and therefore contributes zero to the Wronskian with `u_-`; its remaining lower-order effect is already negligible in (8).

## 3. The left connection coefficient cancels

Let `r_n(a)` be the regular solution selected by the left endpoint/boundary condition of the parity block. Since `-a^2` belongs to the resolvent set of the positive operator `L`, `r(a)` cannot be square summable at infinity. Therefore its dominant coefficient is nonzero:

\[
r_n(a)
=A_\varepsilon(a)u_+(n)+B_\varepsilon(a)u_-(n),
\qquad
A_\varepsilon(a)\ne0.
\tag{10}
\]

At resonance the definition of `u_+` includes the harmless subordinate logarithmic term (6). Equation (10) still implies

\[
r_n(a)
=A_\varepsilon(a)n^{\rho_+}
\left(1+O_a(n^{-1})\right)
\tag{11}
\]

because `u_-` and `u_-\log n` are lower order by more than two powers.

Let `u_-` be the right/Weyl solution. The standard Jacobi Green formula gives, for `i\le j`,

\[
G_{ij}^{(\varepsilon)}(a)
:=
\langle e_{2i+\varepsilon},(L+a^2)^{-1}e_{2j+\varepsilon}\rangle
=
\frac{r_i(a)u_-(j)}{W(r,u_-)}.
\tag{12}
\]

Bilinearity of the Wronskian, (9), and (10) give

\[
W(r,u_-)
=A_\varepsilon(a)W(u_+,u_-)
=2\mu A_\varepsilon(a).
\tag{13}
\]

The same unknown connection coefficient `A_\varepsilon(a)` appears in the numerator through (11), so it cancels exactly. Using (5) yields

\[
G_{ij}^{(\varepsilon)}(a)
=
\frac1{2\mu}
i^{\rho_+}j^{\rho_-}
\left(1+O_a(i^{-1})+O_a(j^{-1})\right),
\tag{14}
\]

which is (1).

The sign is consistent with positivity. In the PF-247 parity representation the Jacobi off-diagonals are negative; for the negative spectral point `-a^2`, the Green kernel in this gauge is positive, and the leading coefficient `1/(2\mu)` is positive.

## 4. Separated-cone consequence after the PF-261 endpoint weights

Equation (1) already exposes the correct moving-source geometry. On any fixed separated cone `j\ge\lambda i` with `\lambda>1`,

\[
G_{ij}^{(\varepsilon)}(a)
\sim
\frac1{2\mu}
\frac1{\sqrt{ij}}
\left(\frac{i}{j}\right)^\mu.
\tag{15}
\]

Thus larger mass strengthens the **ratio decay**, not merely the fixed-row tail. PF-261 inserts the additional diagonal factor

\[
\frac1{\sqrt{\kappa_{2i+\varepsilon}\kappa_{2j+\varepsilon}}}
\sim\frac1{2\sqrt{ij}}.
\tag{16}
\]

For one fixed mass term of PF-261's off-diagonal Green sum, the two-index leading profile is therefore proportional to

\[
\frac{a^2}{\mu}\,
i^{\mu-1}j^{-\mu-1}
=
\frac{a^2}{\mu}\,j^{-2}
\left(\frac{i}{j}\right)^{\mu-1}.
\tag{17}
\]

In particular, for `j\ge2i`, the leading profile gains the explicit mass damping

\[
\left(\frac{i}{j}\right)^{\mu-1}
\le2^{1-\mu}.
\tag{18}
\]

This is exactly the qualitative behavior needed for the odd mass ladder: high masses become *easier* in a genuinely separated cone. But (18) is only a consequence of the fixed-mass asymptotic. It is not yet legitimate to insert it under the infinite PF-261 sum because the `O_a(\cdot)` remainder has not been controlled uniformly as `a` moves with `i`, `j`, and `s`.

## 5. What this removes from the live obstruction

PF-262 left two intertwined uncertainties: the source-dependent Green connection coefficient and the mass dependence. The first is now structurally understood at fixed mass. Once the source index itself enters the asymptotic region, its dominant connection coefficient cancels from the Green formula and leaves the universal factor `1/(2\mu)`.

The live obstruction is therefore more specific than “control the Green connection coefficient.” What is missing is a **parameter-uniform version of the two-solution asymptotics/Wronskian reduction** in the coupled region relevant to the finite seam. A useful theorem would make the errors in (1) uniform when `a` is allowed to vary with the indices, at least after splitting the mass range into regimes such as `a\lesssim i`, `i\lesssim a\lesssim j`, and `a\gtrsim j`.

The leading law strongly suggests that the large-mass regime should not be the dangerous one on a separated cone: (18) supplies exponential-in-`\mu` ratio damping. The real question is whether a uniform theorem reaches that leading regime before its constants grow fast enough to erase the damping.

## 6. Prior art and novelty audit

The ingredients are classical. NIST DLMF §2.9(ii) records the coincident-characteristic-value asymptotic theory used in PF-262/PF-263. The discrete Wronskian and Green-function factorization by a left regular solution and a right Weyl solution are standard Jacobi-operator theory; see G. Teschl, *Jacobi Operators and Completely Integrable Nonlinear Lattices*, Mathematical Surveys and Monographs 72, AMS (2000), especially the foundational Weyl/Green theory for second-order difference expressions.

A targeted literature search also located the general critical double-root Jacobi theory of J. Janas, S. Naboko, and E. Sheronova, *Asymptotic Behavior of Generalized Eigenvectors of Jacobi Matrices in the Critical (Double Root) Case*, Z. Anal. Anwend. 28 (2009), 411--430, DOI `10.4171/ZAA/1391`.

No novelty is claimed for Wronskian constancy, Weyl-solution Green formulas, Birkhoff--Adams asymptotics, or their generic combination. The project-specific statement is the substitution of PF-262's exact leading Jacobi coefficients and indicial pair, for which `p_n\sim-n^2` and `\rho_++\rho_-=-1` make the Wronskian limit **exactly `2\mu`** and cancel the unknown Prime-Flute parity connection coefficient. A targeted search did not locate this specific two-index law for the PF fixed-axis operator or a parameter-uniform theorem strong enough to close the PF-261 mass sum.

## 7. Boundaries and adversarial checks

1. **Fixed mass.** The `O_a` remainders are not uniform in `a`. Equation (1) cannot yet be summed over PF-261's `a_k`.
2. **Both indices asymptotic.** PF-262/PF-263 remain the correct statements for a fixed source row. Equation (1) requires `i\to\infty` as well as `j\to\infty`.
3. **No interchange of limits and the mass series.** The limit `i,j\to\infty` at each fixed `a_k` does not justify passing the limit through the infinite `k`-sum.
4. **Resonant log checked.** At integer difference, the logarithm is attached to the dominant solution as a multiple of `u_-`; it vanishes from `W(u_+,u_-)` and is lower order in the numerator. It does not change the coefficient in (1).
5. **Boundary coefficient cannot vanish.** `A_\varepsilon(a)=0` would make the left regular solution square summable and produce an eigenvector at `-a^2`, impossible because `L+a^2>0`.
6. **Parity normalization checked.** The universal Wronskian coefficient comes from the parity-index recurrence `p_n\sim-n^2` of PF-262. The physical Gegenbauer mode is `2n+\varepsilon`; the separate factor (16) accounts for that mode normalization when returning to PF-261.
7. **No Robin/global conclusion.** Even a uniform Green theorem still has to be propagated through the combined bounded Robin transform, actual corridor/hypercycle transport, PF-243 reassembly, and the global weak-trace target.

The finding is falsified if the PF-262 parity recurrence has a different leading Wronskian normalization, if the regular solution can lose its dominant component at the negative resolvent point, or if a resonant logarithm changes the recessive Wronskian. Under the stated fixed-mass hypotheses, the standard recurrence identities exclude all three.

## Decisive next test

Prove or refute a **uniform version of (1)** in the separated cone `j\ge2i+2` after splitting the mass parameter relative to the indices. The strongest useful target is a bound of the schematic form

\[
|G_{ij}^{(\varepsilon)}(a)|
\le
\frac{C}{\mu\sqrt{ij}}
\left(\frac{i+1}{j+1}\right)^{c\mu}
\tag{19}
\]

with constants independent of `a`, `i`, and `j` in the canonical tail and some fixed `c>0`. Even a weaker bound retaining enough of the ratio exponent to sum the PF-261 odd mass ladder would materially close the accepted finite-seam clue. If uniformity fails, identify the precise transition regime in `a/i` where the fixed-mass Wronskian law ceases to control the connection problem.