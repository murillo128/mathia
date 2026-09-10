# AF-238 — completed Li jets still create a root-rate artifact

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `RH-SUFFICIENT-QUOTIENT`, `TARGET-METRIC`, `CANCELLATION-COHERENCE`, `PRECONDITIONING-NO-GO`, `NO-NOVELTY-CLAIM`

## Claim

AF-237 shows that a fixed positive initial fraction of the local `eta` jet can acquire a spurious exponential root rate from the first trivial zeta zero. A natural repair is to absorb the entire explicit completion before truncating, so that trivial zeros are no longer singularities of the local logarithmic derivative. That repair is not sufficient.

Let

\[
\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

and expand its completed logarithmic derivative at `s=1`:

\[
Q(w):=\frac{\xi'}{\xi}(1+w)
      =\sum_{j\ge0} b_j w^j.
\tag{1}
\]

The Li differential formula gives the exact completed-jet transform

\[
\lambda_n
=\sum_{k=1}^n \binom nk b_{k-1}.
\tag{2}
\]

For `K_n\le n`, define the initial completed-jet truncation

\[
L_n^{\le K}:=\sum_{k=1}^{K_n}\binom nk b_{k-1}.
\tag{3}
\]

Let

\[
\rho_1=\frac12+i\gamma_1,
\qquad
\gamma_1\approx14.13472514173469379,
\]

be the first nontrivial zeta zero and put

\[
a:=\rho_1-1=-\frac12+i\gamma_1,
\qquad
R:=|a|=\sqrt{\frac14+\gamma_1^2}
\approx14.1435658457.
\tag{4}
\]

The first zero and its conjugate are known unconditionally to be simple and on the critical line. For every fixed

\[
0<\alpha<\alpha_*:=\frac1{R+1}
\approx0.06603464535,
\qquad
K_n=\lfloor\alpha n\rfloor,
\tag{5}
\]

one has the exact root-rate asymptotic

\[
\boxed{
\limsup_{n\to\infty}
|L_n^{\le\lfloor\alpha n\rfloor}|^{1/n}
=
\frac{e^{H(\alpha)}}{R^\alpha}
>1,
}
\tag{6}
\]

where

\[
H(\alpha)=-\alpha\log\alpha-(1-\alpha)\log(1-\alpha).
\tag{7}
\]

Thus **removing the zeta pole, every trivial zero, and the whole gamma/completion contribution before truncation does not make an initial linear jet cancellation-coherent**. It only moves the dominant truncation artifact from the first trivial zero at distance `3` (AF-237) to the nearest nontrivial zero pair at distance `R\approx14.14`.

The point is especially sharp because this nearest pair is already known to lie on the critical line. Its contribution to the **full** Li transform has root rate `1`, exactly the harmless AF-235 scale, whereas interrupting its binomial orbit at any fixed fraction `0<\alpha<\alpha_*` creates root rate strictly greater than `1`. The exponential class in `(6)` is therefore a truncation artifact produced by a target-compatible zero, not evidence of an off-critical zero.

## Derivation

### The completed local jet gives the full Li coefficient

Write

\[
\log\xi(1+w)=C+\sum_{k\ge1}\frac{b_{k-1}}{k}w^k.
\tag{8}
\]

Li's differential functional is

\[
\lambda_n
= n[w^n](1+w)^{n-1}\log\xi(1+w).
\tag{9}
\]

The constant term contributes nothing because `(1+w)^{n-1}` has degree `n-1`. Hence

\[
\begin{aligned}
\lambda_n
&=n\sum_{k=1}^n\frac{b_{k-1}}k\binom{n-1}{k-1}\\
&=\sum_{k=1}^n\binom nk b_{k-1},
\end{aligned}
\tag{10}
\]

which proves `(2)`. Unlike AF-236/AF-237, no explicit completion term remains outside the truncation: the source germ is already `\xi'/\xi`.

### The nearest completed singularities are the first nontrivial zero pair

The function `xi` is entire and its zeros are exactly the nontrivial zeros of `zeta`, so `Q` is meromorphic with poles at

\[
w_\rho=\rho-1.
\tag{11}
\]

Rigorous zero verification places the first zeros at

\[
\frac12\pm i\gamma_1,
\qquad
\gamma_1\approx14.1347251417,
\]

with the next pair at ordinate about `21.0220396388`; the verified low zeros are simple and lie on the critical line. Therefore the two poles `a,\bar a` are the unique nearest singularities of `Q`, both of residue `1`, and there is some `R_2>R` such that

\[
C(w):=Q(w)-\frac1{w-a}-\frac1{w-\bar a}
\tag{12}
\]

is analytic on `|w|<R_2`.

The pole expansions are

\[
\frac1{w-a}=-\sum_{j\ge0}\frac{w^j}{a^{j+1}},
\qquad
\frac1{w-\bar a}=-\sum_{j\ge0}\frac{w^j}{\bar a^{j+1}}.
\tag{13}
\]

Consequently the contribution of the nearest pair to `(3)` is

\[
P_{n,K}
=-\sum_{k=1}^K\binom nk\left(a^{-k}+\bar a^{-k}\right).
\tag{14}
\]

### A complex nearest pole still gives endpoint-dominated exponential growth

Consider first one pole and set

\[
T_{n,K}(a):=\sum_{k=1}^K\binom nk a^{-k}.
\tag{15}
\]

Take `K=K_n=floor(alpha n)` and assume `alpha<1/(R+1)`. If

\[
t_{n,k}=\binom nk a^{-k},
\]

then for each fixed `r>=0`,

\[
\frac{t_{n,K-r}}{t_{n,K}}
\longrightarrow
\left(\frac{\alpha a}{1-\alpha}\right)^r.
\tag{16}
\]

Moreover

\[
\left|\frac{\alpha a}{1-\alpha}\right|<1.
\tag{17}
\]

The same ratio is uniformly bounded away from `1` for the reversed tail once `n` is large, so dominated geometric summation gives

\[
\frac{T_{n,K}(a)}{\binom nK a^{-K}}
\longrightarrow
\frac1{1-q_\alpha},
\qquad
q_\alpha:=\frac{\alpha a}{1-\alpha}.
\tag{18}
\]

Write `a=Re^{i\theta}` and `C_\alpha=(1-q_\alpha)^{-1}`. Combining the conjugate poles,

\[
P_{n,K}
=-2\binom nK R^{-K}
\left(\Re(C_\alpha e^{-iK\theta})+o(1)\right).
\tag{19}
\]

Because `0<alpha<1`, the integer sequence `floor(alpha n)` reaches every sufficiently large integer: its increments are only `0` or `1` and it tends to infinity. The sequence

\[
\Re(C_\alpha e^{-ik\theta})
\]

therefore has an infinite subsequence bounded away from zero. If `theta/pi` is rational this follows from periodicity and nontriviality; if it is irrational it follows from density on the circle. Hence Stirling's formula yields

\[
\limsup_{n\to\infty}|P_{n,K_n}|^{1/n}
=
\frac{e^{H(\alpha)}}{R^\alpha}.
\tag{20}
\]

### Everything beyond the nearest pair is exponentially smaller

Choose

\[
R<R'<\min\left\{R_2,\frac{1-\alpha}{\alpha}\right\},
\tag{21}
\]

which is possible precisely because `alpha<1/(R+1)`. If

\[
C(w)=\sum_{j\ge0}c_jw^j,
\]

Cauchy's estimate gives `|c_j|<=M_{R'}(R')^{-j}`. The same endpoint estimate used above then gives for the corresponding truncated remainder `E_{n,K_n}`

\[
\limsup_{n\to\infty}|E_{n,K_n}|^{1/n}
\le
\frac{e^{H(\alpha)}}{(R')^\alpha}
<
\frac{e^{H(\alpha)}}{R^\alpha}.
\tag{22}
\]

Thus the analytic remainder cannot cancel the nearest-pair limsup, proving the equality in `(6)`.

Finally define

\[
f(\alpha)=H(\alpha)-\alpha\log R.
\]

For `0<alpha<1/(R+1)`,

\[
f'(\alpha)=\log\frac{1-\alpha}{\alpha R}>0,
\tag{23}
\]

while `f(0+)=0`. Therefore `f(alpha)>0`, which proves the strict inequality in `(6)`.

### Full depth cancels the same pair back to root rate one

For one pole,

\[
-\sum_{k=1}^n\binom nk a^{-k}
=1-\left(1+\frac1a\right)^n
=1-\left(\frac{\rho_1}{\rho_1-1}\right)^n.
\tag{24}
\]

Since `Re(rho_1)=1/2`,

\[
|\rho_1|=|\rho_1-1|,
\tag{25}
\]

so the exponential factor in `(24)` has modulus exactly `1`. Adding the conjugate pole stays bounded. The nearest known critical-line pair therefore changes from a bounded full-depth contribution to the exponentially growing partial contribution `(6)` solely because the binomial cancellation was interrupted.

## Why completion does not solve the AF-237 problem

AF-237 left open the most obvious escape: package the known pole, gamma factor, and trivial-zero structure into `xi` before truncation. Equation `(6)` closes that escape for ordinary initial fixed-fraction jets.

Completion removes a **known irrelevant singularity family**, but it does not turn the Li transform into a monotone accumulation of locally useful information. Nontrivial zeros on the critical line are themselves harmless for the AF-235 root-rate decoder only after their complete binomial orbit is assembled. An initial local jet sees the large intermediate binomial terms without the later terms that restore modulus-one behavior.

Thus the relevant resource is stronger than "remove the trivial zeros first":

\[
\boxed{\text{cancellation coherence must respect target-valid singularities as well.}}
\tag{26}
\]

A preprocessing that removes the nontrivial zero pair itself would of course cure this particular artifact, but doing so requires precisely the zero data the RH-facing source bridge is supposed to avoid importing. It is not an admissible cheap repair merely because the first pair is numerically known.

## Matched controls and boundaries

**Zeta-germ control.** AF-237 has the same phenomenon with the uncompleted `eta` germ. Its nearest pole is the trivial zero at distance `3`, and endpoint dominance holds for `alpha<1/4`. Completion moves the first proven artifact window down to approximately `alpha<0.066`, but does not eliminate it.

**Full-depth control.** Equation `(24)` shows exactly what the truncation breaks. The same nearest pole that creates root rate greater than `1` at small fixed fractions gives only modulus-one oscillation after full binomial summation.

**Sublinear control.** For any analytic germ, the AF-236 entropy estimate makes every `K_n=o(n)` initial truncation subexponential. The completed germ therefore has the same qualitative phase: sublinear depth is invisible, while sufficiently small positive linear depth becomes spuriously exponential.

**Saddle boundary.** The theorem is proved for `alpha<1/(R+1)`, where the retained endpoint dominates the complex incomplete binomial sum. The numerical value `alpha_*≈0.0660346` is a proof/saddle boundary, not a claim that larger fractions are faithful. Beyond it, interior saddle cancellation must be analyzed separately.

**Nearest-zero data are used only to diagnose the approximation.** The construction of `L_n^{<=K}` itself uses derivatives of the standard completed function at `s=1`; it does not insert a zero. The proof identifies the existing nearest poles to explain why the approximation fails. This is a falsification of the truncation, not a zero-based construction of an RH surrogate.

**No implication about RH truth.** The first zero pair is rigorously known to lie on the critical line. The theorem therefore uses no hypothetical off-critical zero. It says that the truncated surrogate belongs to the wrong AF-235 exponential class for structural reasons, not that the actual Li sequence does.

## Prior art and novelty assessment

The completed function, Li differential formula, and Keiper/Li power-series framework are classical. Jerry B. Keiper, **“Power Series Expansions of Riemann's xi Function,”** *Mathematics of Computation* 58(198), 765–773 (1992), DOI `10.1090/S0025-5718-1992-1122072-5`, is the primary source already used in AF-235 for the relevant completed generating functions.

Dave Platt and Tim Trudgian, **“The Riemann hypothesis is true up to 3·10^12,”** *Bulletin of the London Mathematical Society* 53(3), 792–797 (2021), DOI `10.1112/blms.12460`, rigorously verify with interval arithmetic that all zeta zeros through that height are on the critical line and simple. The LMFDB Riemann-zeta entry lists the first ordinates `14.134725141734...`, `21.022039638771...`, and subsequent zeros; together these facts justify the isolated nearest-pair input used above.

Endpoint asymptotics for incomplete binomial sums and singularity-dominance arguments are classical analytic tools. A targeted search of Li/Keiper, completed-xi Taylor-coefficient, and incomplete-binomial literature did not locate the specific fixed-fraction completed-jet statement `(6)`. No literature novelty claim is made. The durable Arithmetic Fidelity result is the exact obstruction: **even after full classical completion, an initial fixed positive local jet can manufacture an RH-decisive exponential class from a zero already known to be on the critical line.**

## Evidence boundary

Equation `(6)` is an unconditional asymptotic statement for the canonical completed local-jet truncation `(3)` in the declared range `0<alpha<1/(R+1)`. It uses the classical Li differential representation, the rigorously verified first critical-line zero pair, local meromorphic expansion, elementary incomplete-binomial asymptotics, Cauchy estimates, and Stirling's formula.

The finding does not classify `alpha>=alpha_*`, prove that no cancellation-coherent compression exists, price numerical precision for completed derivatives, or provide a prime-side estimate. It does not establish a new RH criterion or any evidence for RH itself.

In particular, the theorem rules out **naive initial truncation after completion**, not completion as a mathematical tool. A different filter could succeed only by proving that it preserves the complete cancellation required for every target-valid singularity while remaining sensitive to a hypothetical mapped pole corresponding to an off-critical zero.

## Consequences for the research frontier

AF-236 and AF-237 can now be sharpened into a three-part source-access constraint for the Li root-rate quotient. Sublinear initial depth cannot reach the exponential class; small fixed linear depth can create the wrong class; and explicit completion removes only the trivial-zero version of that failure, not the underlying cancellation problem.

The next useful source bridge should therefore be tested as a **filter-separation problem**, not merely as a deeper truncation. A candidate aggregation of local completed data must simultaneously suppress the exponential partial-sum response of every critical-line pole (whose full Cayley image has modulus one) while retaining exponential sensitivity to any off-critical pole whose Cayley image lies inside the unit disk. The key question is whether such cancellation coherence can be forced by an intrinsic kernel, symmetry, contour representation, or other source-side operation without importing the nontrivial zero divisor. Merely increasing the retained fraction is no longer evidence that the AF-235 quotient is being approached faithfully.