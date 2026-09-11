# AF-271 — Finite prime-power prefixes detect bounded periodic divisor complexity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SOURCE`, `PERIODIC-DIVISOR`, `FINITE-MOMENT-RECOVERY`, `VANDERMONDE`, `STABILITY-BOUNDARY`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-270 shows that exact Bohr recurrence and even the correct rational-prime-power frequency ray do not determine critical-line geometry: a periodic infinite zero transport can stay on one ray `p^k` while changing only the coefficient law. For the important subclass in which the periodic control has **bounded divisor-orbit complexity**, however, the full infinite coefficient law is unnecessary. A finite prefix already detects every nontrivial divisor change.

Fix a rational prime `p`, put

\[
\lambda:=\log p,
\qquad
z:=p^{-s},
\qquad
L:=\frac{2\pi}{\lambda},
\tag{1}
\]

and consider a rational periodic quotient

\[
Q(s)=C z^\nu\prod_{j=1}^{r}(1-\alpha_j z)^{m_j},
\tag{2}
\]

where `C != 0`, `nu in Z`, the `alpha_j in C^*` are pairwise distinct, and the nonzero integers `m_j` are signed zero/pole multiplicities. The `r` distinct factors are exactly the distinct nonconstant divisor orbits modulo the vertical period `iL`.

On every right half-plane satisfying

\[
|\alpha_j p^{-s}|<1
\qquad(1\le j\le r),
\tag{3}
\]

the logarithmic derivative has the prime-power expansion

\[
\boxed{
\frac{Q'}{Q}(s)
=-\nu\lambda
+\lambda\sum_{k\ge1}q_k p^{-ks},
\qquad
q_k=\sum_{j=1}^{r}m_j\alpha_j^k.
}
\tag{4}
\]

Then:

1. **Exact finite detection.** If
   \[
   q_1=q_2=\cdots=q_r=0,
   \tag{5}
   \]
   then all `m_j=0`. Hence a nontrivial quotient with at most `r` divisor orbits must alter at least one of the first `r` coefficients on that prime-power ray.

2. **Sharp dependence on complexity.** No fixed prefix detects arbitrary finite periodic divisor complexity. For every `K>=1` and every `A in C^*`,
   \[
   R_{K+1}(z):=1-(Az)^{K+1}
   \tag{6}
   \]
   has `K+1` distinct divisor orbits and a nontrivial logarithmic derivative whose first `K` prime-power coefficients vanish exactly.

3. **Exact fidelity is not stable without geometric control.** Even at fixed complexity `r=2`, there is no positive coefficient-separation modulus depending only on nontriviality. For
   \[
   Q_\varepsilon(z)
   :=\frac{1-\alpha z}{1-(\alpha+\varepsilon)z},
   \tag{7}
   \]
   every fixed finite coefficient window tends to zero as `epsilon -> 0` although the signed divisor is nontrivial for every `epsilon != 0`.

4. **Separation restores a quantitative modulus.** Suppose additionally
   \[
   0<a\le |\alpha_j|\le b,
   \qquad
   |\alpha_i-\alpha_j|\ge\delta>0
   \quad(i\ne j).
   \tag{8}
   \]
   With `B=max(1,b)`, the first `r` coefficients obey the explicit nonzero lower bound
   \[
   \boxed{
   \left(\sum_{k=1}^{r}|q_k|^2\right)^{1/2}
   \ge
   \frac{a^r\delta^{r(r-1)/2}}
   {(rB^r)^{r-1}}.
   }
   \tag{9}
   \]
   The constant is deliberately crude; its role is to show that compact radial control plus node separation converts exact divisor fidelity into stable finite-prefix fidelity.

Thus AF-270's periodic infinite-transport escape has a precise information bill. **Frequency support alone is too coarse, but bounded periodic divisor complexity is completely audited by a coefficient prefix whose length matches that complexity.** Without a complexity or separation budget, finite coefficient inspection is respectively non-identifying or ill-conditioned.

## Exact derivation

### 1. Periodic divisor orbits become a finite power-sum source

Because `z=p^{-s}` is unchanged by `s -> s+iL`, each factor in `(2)` defines one vertical zero or pole lattice. Logarithmically differentiating gives

\[
\frac{d}{ds}\log z^\nu=-\nu\lambda.
\tag{10}
\]

For a nonconstant factor, whenever `|alpha_j z|<1`,

\[
\begin{aligned}
\frac{d}{ds}\log(1-\alpha_j z)^{m_j}
&=m_j\lambda\frac{\alpha_j z}{1-\alpha_j z}\\
&=m_j\lambda\sum_{k\ge1}\alpha_j^kz^k.
\end{aligned}
\tag{11}
\]

Summing `(11)` proves `(4)`. The nonconstant source coefficients are therefore the power moments of the finite signed atomic divisor measure

\[
\mu_Q:=\sum_{j=1}^{r}m_j\delta_{\alpha_j}.
\tag{12}
\]

This is the exact point at which the periodic zero problem enters classical finite-moment/Prony geometry.

### 2. The first `r` vanishing coefficients force the divisor to vanish

Let

\[
q=(q_1,\ldots,q_r)^T,
\qquad
m=(m_1,\ldots,m_r)^T,
\tag{13}
\]

and define

\[
V_{kj}:=\alpha_j^k,
\qquad
1\le k,j\le r.
\tag{14}
\]

Then `(4)` gives simply

\[
q=Vm.
\tag{15}
\]

The determinant is

\[
\det V
=\left(\prod_{j=1}^{r}\alpha_j\right)
\prod_{1\le i<j\le r}(\alpha_j-\alpha_i),
\tag{16}
\]

up to the conventional sign of the Vandermonde product. Every factor is nonzero because the nodes are distinct and lie in `C^*`. Hence `V` is invertible. Equation `(5)` therefore implies `m=0`, proving the exact finite-detection statement.

Notice what is and is not being reconstructed. The theorem does not claim that `r` arbitrary nonzero moments identify unknown nodes and weights numerically. Classical Prony reconstruction normally uses a longer moment window to recover those parameters. The present target is weaker and sharper for the fidelity question: **if two controls of known signed-divisor complexity at most `r` agree on the first `r` source coefficients, their quotient cannot contain any nonconstant divisor orbit at all.**

### 3. No coefficient prefix is universal without a complexity bound

Set

\[
r:=K+1.
\tag{17}
\]

Factor `(6)` over the `r`th roots of unity:

\[
1-(Az)^r
=\prod_{j=0}^{r-1}(1-A\omega_r^jz),
\qquad
\omega_r=e^{2\pi i/r}.
\tag{18}
\]

Thus the quotient has exactly `r` distinct divisor nodes `alpha_j=A omega_r^j`. Its logarithmic derivative is

\[
\begin{aligned}
-\lambda z\frac{d}{dz}\log(1-(Az)^r)
&=\lambda r\frac{(Az)^r}{1-(Az)^r}\\
&=\lambda r\sum_{n\ge1}A^{rn}z^{rn}.
\end{aligned}
\tag{19}
\]

All source coefficients of degrees `1,...,r-1=K` therefore vanish, while the coefficient of degree `r` equals `rA^r` and the divisor is nontrivial. This proves that **finite-prefix sufficiency necessarily carries an orbit-complexity hypothesis**. Merely knowing that a source is periodic, rational in `p^{-s}`, or supported on one rational-prime ray does not give a universal finite certificate.

### 4. Exact detection can be arbitrarily ill-conditioned

For `(7)`, formula `(4)` gives

\[
q_k(\varepsilon)
=\alpha^k-(\alpha+\varepsilon)^k.
\tag{20}
\]

For every fixed `K`,

\[
\max_{1\le k\le K}|q_k(\varepsilon)|\to0
\qquad(\varepsilon\to0),
\tag{21}
\]

while the zero and pole nodes remain distinct whenever `epsilon != 0`. Hence there is no positive lower modulus separating all nontrivial finite-orbit divisor edits from the zero coefficient vector. This is exactly the familiar collision instability of Vandermonde/Prony inversion, here interpreted as an Arithmetic Fidelity boundary.

The example also explains why the exact statement `(5)` must not be silently upgraded to a robust one. A source prefix can be logically complete and still be useless at finite precision when divisor nodes nearly collide.

### 5. A separated compact class has a uniform finite-prefix gap

Under `(8)`, equation `(16)` gives

\[
|\det V|
\ge
 a^r\delta^{r(r-1)/2}.
\tag{22}
\]

Every entry satisfies

\[
|V_{kj}|=|\alpha_j|^k\le B^r,
\tag{23}
\]

so

\[
\|V\|_2\le\|V\|_F\le rB^r.
\tag{24}
\]

If `sigma_1>=...>=sigma_r>0` are the singular values, then

\[
|\det V|=\prod_{j=1}^{r}\sigma_j
\le \|V\|_2^{r-1}\sigma_r.
\tag{25}
\]

Therefore

\[
\sigma_{\min}(V)
\ge
\frac{a^r\delta^{r(r-1)/2}}
{(rB^r)^{r-1}}.
\tag{26}
\]

The multiplicity vector is a nonzero integer vector, hence `||m||_2>=1`. Combining `(15)` and `(26)` proves `(9)`.

The integer-multiplicity hypothesis matters for this absolute modulus. With arbitrary complex weights one must instead normalize the weight vector, and the lower bound scales with that norm. In the divisor application integer residues provide the normalization intrinsically.

## Application to the AF-270 periodic escape

For `a != 1/2`, the quotient between the AF-270 controls

\[
\frac{H_a}{H_{1/2}}
\tag{27}
\]

is rational in `z=p^{-s}` up to a constant/monomial factor and has three distinct signed divisor nodes

\[
\alpha_1=p^a,
\qquad
\alpha_2=p^{1-a},
\qquad
\alpha_3=p^{1/2},
\tag{28}
\]

with signed multiplicities `(+1,+1,-2)`. Its source difference is

\[
q_k
=p^{ka}+p^{k(1-a)}-2p^{k/2},
\tag{29}
\]

exactly the coefficient profile isolated in AF-270.

The general theorem says that agreement with the critical control through the first three prime powers would already force the signed divisor to vanish. This particular family is even easier: strict convexity gives `q_k>0` for every `k>=1`, so the first coefficient already sees the split.

The important conclusion is not that three coefficients solve the global zeta problem. It is that AF-270's counterexample does **not** force Arithmetic Fidelity all the way from support information to the exact infinite von-Mangoldt law. There is an intermediate source resource:

\[
\boxed{
\text{bounded periodic divisor complexity}
+\text{matching finite coefficient prefix}
\Longrightarrow
\text{no periodic divisor surgery}.
}
\tag{30}
\]

Conversely, `(18)` shows exactly how an adversary escapes any fixed prefix: increase the periodic divisor complexity beyond the inspected moment order. The next genuinely global question is therefore whether an RH-violating source-compatible control can have **unbounded/infinite effective divisor complexity while still satisfying the structural restrictions of the zeta source**, rather than merely whether it can stay recurrent on the correct frequency alphabet.

## Prior art and novelty assessment

The recovery mathematics is classical. Prony's method reconstructs finitely supported exponential sums or atomic measures from moment samples; the Vandermonde argument in `(15)` is its elementary exact core. Stefan Kunis, Thomas Peter, Tim Römer, and Ulrich von der Ohe, **“A multivariate generalization of Prony's method,”** *Linear Algebra and its Applications* 490 (2016), 31–47, DOI `10.1016/j.laa.2015.10.023`, explicitly places finite-support parameter reconstruction from moments in that classical Prony lineage.

The stability boundary is likewise classical Vandermonde conditioning. Fermín S. V. Bazán, **“Conditioning of Rectangular Vandermonde Matrices with Nodes in the Unit Disk,”** *SIAM Journal on Matrix Analysis and Applications* 21(2), 679–693 (2000), DOI `10.1137/S0895479898336021`, gives bounds depending on node separation and discusses the conditioning of Vandermonde systems used in frequency estimation and system identification. Modern super-resolution/Prony literature sharpens these collision-dependent stability laws substantially.

No novelty is claimed for Prony reconstruction, Newton/power-sum identities, Vandermonde invertibility, or separated-node conditioning. The Arithmetic Fidelity contribution is the **specific audit of AF-270's prime-ray periodic escape**: divisor-orbit complexity becomes the exact budget determining how many prime-power source coefficients are needed merely to rule out a nontrivial rational periodic divisor quotient. The roots-of-unity family `(18)` shows that this budget is not an artifact of the proof.

## Boundaries and failure modes

- The theorem applies to quotients rational in the periodic coordinate `z=p^{-s}` after the harmless monomial/constant ambiguity is separated. A general periodic or almost-periodic zero-free factor can contribute source coefficients without changing the divisor and falls outside this finite-divisor calculation.
- The bound concerns the number of **distinct signed divisor nodes after cancellation**, not the total multiplicity. Repeated multiplicity changes the integer weight `m_j` but does not increase the Vandermonde dimension.
- Exact prefix agreement detects the absence of the divisor quotient; approximate agreement is unstable without radial and separation control, as `(7)` shows.
- The roots-of-unity escape proves that no fixed prefix handles unbounded finite orbit complexity. It does not construct a zeta-like global control satisfying the full Euler coefficient laws, completion, and analytic constraints.
- Different primes can couple through a global control. A one-ray theorem does not classify distributed perturbations involving infinitely many prime rays.
- The AF-270 application is a matched-control audit, not an RH implication. The remaining hard problem is to derive a non-tautological arithmetic bound on effective source/divisor complexity from zeta-specific structure.

## Consequence for the research line

AF-270 ended with a binary-looking boundary: prime-power support is too weak, while the exact source coefficient law may be rigid enough. AF-271 inserts a strict intermediate layer.

For periodic rational controls of bounded orbit complexity, **only finitely many local coefficient weights are needed**, and the required prefix length is controlled by divisor complexity. The obstruction to a finite source certificate is therefore not periodicity itself but unbounded effective complexity; the obstruction to a *stable* finite certificate is additionally node collision or loss of compact radial control.

This reframes the live Arithmetic Fidelity question from "which exact coefficient law must be retained?" to the sharper and potentially more tractable problem:

> Can the genuine zeta source impose an independently justified bound, sparsity law, recurrence rank, or other compactness principle on admissible prime-ray divisor/source complexity, or must every RH-relevant alternative necessarily escape through unbounded distributed complexity?

A positive bound would turn a finite prime-power coefficient window into a complete audit for that control class. A negative construction would identify precisely why local source prefixes cannot replace the global Euler law.