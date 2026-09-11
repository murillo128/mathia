# MC-217 — Matched random multiplicative signs put square-defect raw energy at diagonal scale

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `MATCHED-CONTROL`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-209` reduces the primorial-shift square-defect route to the raw prescribed-residue shell energy

\[
W_D
:=
\sum_{\substack{D<d\le2D\\
\mu^2(d)=1\\
(d,q)=1\\
d^2\le X}}
 d\,|A_d(T)|^2,
\qquad
A_d(T)
:=
\sum_{\substack{n\le T\\(n,q)=1\\d^2\mid n+q}}\mu(n),
\tag{1}
\]

at

\[
y=c\log X,
\qquad
q=\prod_{p\le y}p,
\qquad
T=X-q.
\tag{2}
\]

The deterministic target `W_D\ll X^{1+o(1)}` is enough for square-root-scale control of the corresponding defect shell. `MC-210`--`MC-216` show that standard centering, higher residue moments, and explicit selected-character phases do not provide that estimate cheaply: the principal mode can be Mertens-complete, while the visible residue phases are gauge.

There is nevertheless an exact matched-control calibration showing that the raw target itself has the correct power scale for a genuine multiplicative source with exactly the same square-free support as Möbius.

Let `(\xi_p)_p` be independent Rademacher signs and define the classical square-free-supported random multiplicative function

\[
f_\xi(n)
:=
\begin{cases}
\prod_{p\mid n}\xi_p,& n\text{ square-free},\\
0,& p^2\mid n\text{ for some }p.
\end{cases}
\tag{3}
\]

Thus `|f_\xi(n)|=\mu^2(n)` identically, while actual Möbius is the deterministic prime-sign point `\xi_p=-1` for every prime.

Replace only the source sign in `(1)`:

\[
A_d^{\xi}(T)
:=
\sum_{\substack{n\le T\\(n,q)=1\\d^2\mid n+q}}f_\xi(n),
\qquad
W_D^{\xi}
:=
\sum_d d\mu^2(d)|A_d^{\xi}(T)|^2.
\tag{4}
\]

For every active `d`, put

\[
N_d(T)
:=
\#\{n\le T:
 n\text{ square-free},\ (n,q)=1,\ d^2\mid n+q\}.
\tag{5}
\]

Then square-free Walsh orthogonality gives the **exact second moment**

\[
\boxed{
\mathbb E_\xi |A_d^{\xi}(T)|^2=N_d(T).
}
\tag{6}
\]

Consequently

\[
\boxed{
\mathbb E_\xi W_D^{\xi}
=
\sum_d d\mu^2(d)N_d(T)
\ll X
}
\tag{7}
\]

uniformly for every dyadic root shell in the full `MC-209` range. Indeed

\[
N_d(T)\le \frac{X}{d^2}+1,
\tag{8}
\]

so on `D<d\le2D`, with `D^2\ll X`, the two contributions are

\[
X\sum_{D<d\le2D}\frac1d\ll X,
\qquad
\sum_{D<d\le2D}d\ll D^2\ll X.
\tag{9}
\]

Thus the matched multiplicative ensemble places **every raw selected square-modulus shell at diagonal power scale in expectation**, without centering the residue profile, estimating the principal mode separately, or using a large-sieve/BDH theorem.

The calibration can be made simultaneous and almost sure on dyadic ambient scales. Define the total active root energy

\[
\mathcal W_X^{\xi}
:=
\sum_{\substack{d>y\\
\mu^2(d)=1\\
(d,q)=1\\
d^2\le X}}
 d|A_d^{\xi}(T)|^2.
\tag{10}
\]

Summing `(8)` over all root scales gives

\[
\boxed{
\mathbb E_\xi\mathcal W_X^{\xi}
\ll X\log X.
}
\tag{11}
\]

Hence for every fixed `eta>0`, Markov's inequality and Borel--Cantelli on `X=2^j` imply that for almost every one-time choice of all prime signs,

\[
\boxed{
\mathcal W_X^{\xi}\le X^{1+\eta}
}
\tag{12}
\]

for all sufficiently large dyadic `X`. Since every shell energy is nonnegative, the same one-time random multiplicative function satisfies

\[
W_D^{\xi}\le X^{1+\eta}
\tag{13}
\]

**simultaneously for every active root shell** at those scales.

The original square-defect identity also survives with the source replaced by `f_\xi`. Define

\[
\Delta_\xi(X)
:=
\sum_{\substack{n\le T\\(n,q)=1}}
 f_\xi(n)\bigl(1-\mu^2(n+q)\bigr).
\tag{14}
\]

Using the exact square-free indicator expansion

\[
\mu^2(m)=\sum_{d^2\mid m}\mu(d)
\tag{15}
\]

and the fact that any contributing `d>1` is automatically coprime to `q` and exceeds `y`, one gets

\[
\Delta_\xi(X)
=-
\sum_{\substack{d>y\\(d,q)=1\\d^2\le X}}
\mu(d)A_d^{\xi}(T).
\tag{16}
\]

Weighted Cauchy--Schwarz therefore gives

\[
|\Delta_\xi(X)|^2
\le
\left(\sum_{y<d\le\sqrt X}\frac{\mu^2(d)}d\right)
\mathcal W_X^{\xi}
\ll
(\log X)\mathcal W_X^{\xi}.
\tag{17}
\]

Combining `(12)` and `(17)`, for almost every fixed random multiplicative source and every `epsilon>0`,

\[
\boxed{
\Delta_\xi(X)=O_{\xi,\epsilon}(X^{1/2+\epsilon})
}
\tag{18}
\]

along all sufficiently large dyadic scales.

This is a matched-control result, not a Möbius bound. It shows something structurally useful about the current frontier: **the raw `MC-209` energy theorem is probabilistically natural at the desired power scale even after exact multiplicativity, rational-prime locations, square-free support, the primorial pre-sieve, and the source-prescribed square-modulus incidences are retained.** The unresolved arithmetic obligation is therefore narrower than proving that such cancellation can occur in a multiplicative model. One must control why the single deterministic parity assignment

\[
\xi_p=-1\quad\text{for every prime }p
\tag{19}
\]

does not align abnormally with the lifted incidence family `d^2\mid n+q`.

No estimate for the actual Möbius `W_D`, `\Delta(X)`, `M(X)`, or the zeta zero set is proved here.

## 1. Walsh orthogonality is exact despite multiplicative dependence

For square-free `m,n`,

\[
f_\xi(m)f_\xi(n)
=
\prod_p\xi_p^{\mathbf 1_{p\mid m}+\mathbf 1_{p\mid n}}.
\tag{20}
\]

If `m\ne n`, their prime-factor sets have nonempty symmetric difference, so some independent Rademacher variable appears to the first power and

\[
\mathbb E_\xi[f_\xi(m)f_\xi(n)]=0.
\tag{21}
\]

If `m=n`, the product is identically `1`. Therefore

\[
\boxed{
\mathbb E_\xi[f_\xi(m)f_\xi(n)]
=\mathbf 1_{m=n}
}
\tag{22}
\]

on the square-free support. Expanding `(4)` proves `(6)` immediately.

The exceptional coefficient `f_\xi(1)=1` causes no problem: `(22)` remains valid, and `(6)` is a second-moment identity rather than a zero-mean variance statement. If `d^2\mid q+1`, the term `n=1` is simply one member of `N_d(T)`.

This is the same classical Walsh-character mechanism used in `MC-034`, but the specialization is different. `MC-034` calibrated the Huxley--Watt annular Fourier functional after product-fiber reduction; here the characters are evaluated directly on the **current square-defect selected-progressions**, and the result reaches the exact raw-energy theorem surface isolated only later in `MC-209`.

## 2. The matched control preserves the source geometry that survives the gauge no-go

The randomization changes only prime signs. It does not move integers, alter rational-prime locations, change square-free support, change the primorial `q`, or alter any lifted relation

\[
n+q=d^2m.
\tag{23}
\]

In particular the exact cross-modulus incidence geometry survives. If

\[
N_{d,e}(T)
:=
\#\{n\le T:
 n\text{ square-free},\ (n,q)=1,\
 d^2\mid n+q,\ e^2\mid n+q\},
\tag{24}
\]

then

\[
\boxed{
\mathbb E_\xi[A_d^{\xi}(T)A_e^{\xi}(T)]
=N_{d,e}(T)
=N_{\operatorname{lcm}(d,e)}(T).
}
\tag{25}
\]

Thus the control does **not** destroy the non-equivariant integer lift singled out after `MC-216`; it retains its full unsigned intersection pattern. What it removes is deterministic parity alignment with that pattern.

This gives a sharper interpretation of the post-`MC-216` frontier. Pure lift incidence, even across many square moduli, is not by itself a deterministic cancellation mechanism: the same incidence system supports an ensemble whose exact second moment is already diagonal. Any Möbius-specific theorem must use how the fixed parity character `(-1)^{\omega(n)}` couples to those incidences, not merely the incidence counts themselves.

## 3. Almost-sure simultaneous shell control is only a first-moment argument

From `(7)`, one could apply Markov separately to each shell. It is cleaner to sum the nonnegative shell energies first. Equations `(8)` and `(10)` give

\[
\begin{aligned}
\mathbb E_\xi\mathcal W_X^{\xi}
&\le
X\sum_{d\le\sqrt X}\frac1d
+
\sum_{d\le\sqrt X}d\\
&\ll X\log X.
\end{aligned}
\tag{26}
\]

For `X_j=2^j`,

\[
\mathbb P\!\left(
\mathcal W_{X_j}^{\xi}>X_j^{1+\eta}
\right)
\ll
\frac{j}{2^{\eta j}},
\tag{27}
\]

which is summable. The first Borel--Cantelli lemma, requiring no independence between scales, proves `(12)`. Because the same prime-sign sample is used at every `j`, this is a genuine one-function matched control rather than a fresh randomization at each scale.

Equation `(17)` then proves `(18)` after choosing the energy exponent slightly smaller than the requested final epsilon. No assertion is made for every integer ambient scale; the dyadic statement is enough to establish the fixed-power calibration.

## 4. Prior-art and novelty audit

Rademacher random multiplicative functions supported on square-free integers are a classical model for Möbius going back to Wintner. Modern work studies their partial sums, moments, limit laws, short intervals, and exponential sums. For example, Soundararajan and Xu, *Central limit theorems for random multiplicative functions*, Journal d'Analyse Mathématique 151 (2023), 343--374, DOI `10.1007/s11854-023-0331-y`, studies sums over structured subsets; Seth Hardy, *Bounds for Exponential Sums With Random Multiplicative Coefficients*, IMRN 2024, 14138--14156, DOI `10.1093/imrn/rnae234`, uses the same square-free-supported Rademacher model for additive exponential sums. The literature also records classical almost-sure square-root-scale upper bounds for ordinary partial sums of the Rademacher model.

No novelty is claimed for the random multiplicative model, Walsh orthogonality, Markov's inequality, Borel--Cantelli, or square-free divisor expansion. A bounded structural search did not identify a standard theorem formulated as the exact `MC-209` source-prescribed square-defect energy `(4)`--`(13)`; regardless, the durable content here is only its explicit matched-control specialization to the current line frontier, not a claim of a new general probability theorem.

This finding also does not replace deterministic arithmetic-progression theory. `MC-209` requires control of actual Möbius, while `MC-210` shows why a standard centered BDH theorem does not automatically control the selected raw coordinate. The random calculation succeeds because averaging is over **prime-sign assignments**, not over residue classes or moduli.

## 5. Boundaries and falsification tests

The control result must not be transferred to actual Möbius. The all-minus prime-sign assignment is one exceptional deterministic Walsh-cube point, and expectation over the cube gives no pointwise estimate there.

The result also does not show that `W_D\ll X^{1+o(1)}` is insufficient for a Möbius argument; on the contrary, `MC-209` proves it would be sufficient for the square-defect shell. It shows only that the power scale is compatible with a very strong matched multiplicative control and therefore needs a **Möbius-specific deterministic explanation** rather than a generic random-sign heuristic.

The exact claims can be falsified finitely:

1. exact averaging over all prime signs active below a finite `T` must give `(6)` for each `d`;
2. joint averaging of two selected sums must give the intersection count `(25)`;
3. direct counting must satisfy `(8)`, and summing it with weight `d` must give `(7)` and `(11)`;
4. the square-free identity `(15)` must reproduce `(16)` for every finite input;
5. deterministic weighted Cauchy--Schwarz must give `(17)` independently of the random model.

A finite computation in which actual Möbius has an unusually large or small ratio

\[
\frac{W_D(\mu)}{\mathbb E_\xi W_D^{\xi}}
\tag{28}
\]

would be a diagnostic only. A substantive continuation requires a deterministic theorem or obstruction controlling that inflation from source arithmetic.

## Consequence for the research line

`MC-213`--`MC-216` progressively remove total transverse magnitude, higher all-residue moments, single-modulus selected phases, and coherent cross-modulus selected phases as cheap explanations for the required principal/transverse interference. The present matched control tests the first surviving non-equivariant object: the actual lifted square-divisor incidence pattern.

That object passes the probabilistic calibration. A one-time multiplicative prime-sign source preserving the exact incidence geometry has `W_D=X^{1+o(1)}` simultaneously on all root shells along dyadic scales almost surely. Therefore the next deterministic question is sharply localized:

**what arithmetic feature of the all-minus parity point controls its correlation with the square-divisor incidence family beyond the unsigned lift geometry already shared by the matched random ensemble?**

Any proposed source covariance should now be tested against the exact normalization `(6)`--`(13)`. If it cannot distinguish the deterministic Möbius parity assignment from typical prime-sign points except by reintroducing an RH-equivalent Mertens quantity, it has not crossed the current frontier.