# PC-388 — primorial boundary windows are rough-number sieves

**Status:** `EXACT-DERIVED` + `LITERATURE-ANCHORED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for support-level mesoscopic boundary restrictions of primorial primitive shells.

PC-386 and PC-387 classify scalar common-anchor chord sums on primitive shells across the supercritical, critical, and subcritical singularity regimes. A natural escape is to stop summing and retain a growing boundary window of primitive vertices as a genuinely non-scalar point cloud. On primorial shells this does retain much more arithmetic information, but the support itself is not new: it is exactly the classical rough-number/primorial-wheel sieve. Before the first rough composite enters, the retained primitive vertices are literally the primes above the sieving threshold.

This gives a sharp boundary for future operator work. A line-forced kernel acting on these vertices may still have nontrivial mathematics, but detecting primes, prime gaps, or rough almost-primes from the **support alone** is tautological sieve information already inserted by the primitive mask. Any candidate RH mechanism must therefore extract additional structure from the forced interactions, cross-scale transport, or another non-scalar operation rather than from the selected boundary index set itself.

## 1. Exact primitive boundary support

Let

\[
N_x:=\prod_{p\le x}p,
\qquad
p_+(x):=\min\{p>x:p\text{ prime}\},
\tag{1}
\]

and view the primitive vertices of the `N_x`-gon as the exponents `a` with `(a,N_x)=1`. For a boundary width `H<N_x`, define

\[
R_x(H):=\{1\le a\le H:(a,N_x)=1\}.
\tag{2}
\]

If `P^-(a)` denotes the least prime factor of `a>1`, then exactly

\[
(a,N_x)=1
\iff
P^-(a)>x.
\tag{3}
\]

Thus `R_x(H)` is `1` together with the `x`-rough integers at most `H`. No asymptotic or geometric approximation is involved: the primitive-root mask on a primorial shell is exactly the Eratosthenes/primorial-wheel sieve in exponent coordinates.

There is an immediate sharp first-composite threshold. If

\[
H<p_+(x)^2,
\tag{4}
\]

then every `a>1` in `R_x(H)` is prime. Indeed, a composite integer with no prime divisor at most `x` has every prime factor at least `p_+(x)`, hence is at least `p_+(x)^2`. Conversely every prime `p` with `x<p\le H` is coprime to `N_x`. Therefore

\[
\boxed{
R_x(H)=\{1\}\cup\{p:x<p\le H,\ p\text{ prime}\}
\qquad(H<p_+(x)^2).
}
\tag{5}
\]

At `H=p_+(x)^2` the first rough composite, `p_+(x)^2`, enters. More generally, if `H<p_+(x)^{k+1}`, every member of `R_x(H)` has at most `k` prime factors counted with multiplicity. The growing primitive boundary therefore passes through the standard rough-almost-prime hierarchy rather than producing a new geometric hierarchy.

## 2. The geometric scales are logarithmic in the shell order

The prime number theorem gives

\[
\log N_x=\vartheta(x)\sim x,
\qquad
p_+(x)\sim x.
\tag{6}
\]

Hence, measured against the enormous shell order `N_x`, the first nontrivial primitive boundary vertex after `a=1` appears only when the window reaches scale

\[
H\asymp \log N_x,
\tag{7}
\]

while the first rough composite cannot appear before

\[
H\asymp (\log N_x)^2.
\tag{8}
\]

Equivalently, for `H=x^u` with fixed `u>0`, three regimes are forced. If `u<1`, then eventually `R_x(x^u)={1}`. If `1<u<2`, then (5) applies and

\[
R_x(x^u)=\{1\}\cup\{p:x<p\le x^u\},
\tag{9}
\]

so in particular

\[
|R_x(x^u)|-1=\pi(x^u)-\pi(x).
\tag{10}
\]

For `u>2`, rough semiprimes and then higher rough almost-primes enter according to the usual sieve hierarchy.

The classical Buchstab asymptotic makes the last statement quantitative. If `u>1` is fixed, then

\[
|R_x(x^u)|
\sim
\omega(u)\frac{x^u}{\log x},
\tag{11}
\]

where `omega` is Buchstab's function, with `omega(u)=1/u` on `1<u\le2` and

\[
(u\omega(u))'=\omega(u-1)
\qquad(u>2).
\tag{12}
\]

For `1<u<2`, (11) reduces to `x^u/(u\log x)`, exactly matching the prime-only description (9).

## 3. A local chord operator becomes an operator on the classical rough-number set

The support-level classicalization persists before any scalar trace is taken. Let a line-forced chord operator on the `N_x` shell have entries

\[
K^{(N_x)}_{a,b}=\kappa_{N_x}(a-b),
\qquad a,b\in R_x(H),
\tag{13}
\]

for any intrinsic rotation-difference kernel `kappa_{N_x}`. When `H<p_+(x)^2`, the matrix (13) is exactly the same kernel restricted to the point set `1` plus the primes in `(x,H]`. Its gap pattern and every support-derived combinatorial invariant are therefore functions of ordinary prime differences by construction.

For the regularized inverse-chord kernel used in PC-386, the geometric part also has a clean local limit. Put `N=N_x` and let `|d|\le H=o(N)`. Then

\[
2\left(\cosh\frac{\tau}{N}-\cos\frac{2\pi d}{N}\right)
=
\frac{\tau^2+4\pi^2d^2}{N^2}
\left(1+O\!\left(\frac{1+d^2}{N^2}\right)\right),
\tag{14}
\]

uniformly on any polylogarithmic boundary window. Consequently, for fixed `alpha`,

\[
N^{-2\alpha}
\left[2\left(\cosh\frac{\tau}{N}-\cos\frac{2\pi d}{N}\right)\right]^{-\alpha}
=
(\tau^2+4\pi^2d^2)^{-\alpha}(1+o(1))
\tag{15}
\]

uniformly there. Thus the prime-circle geometry locally Euclideanizes while the primitive mask supplies the classical rough-number support. In the prime-only zone the resulting non-scalar boundary matrix is simply a Euclidean difference kernel evaluated on actual primes.

This does **not** imply that every such matrix invariant is trivial. It says something narrower and decisive: any claimed prime detection caused merely by which boundary vertices survive is not new information supplied by the chord geometry. Novelty would have to reside in a forced interaction law, a cross-level relation, or another invariant not reducible to the preselected sieve support.

## 4. RH-facing consequence and obstruction

Equation (10) is especially diagnostic. In the entire window `1<u<2`, any estimate for the number of retained primitive boundary vertices is exactly an estimate for a prime-counting difference. For example, an RH-strength fluctuation statement for this count would be a reformulation of classical prime-counting information, not an independently generated geometric criterion.

Likewise, once `u>2`, the natural support statistics are the classical rough-number counting problem governed by Buchstab's identity and its descendants. The primitive shell has not generated a new sieve: it realizes the familiar sieve exactly as a subset of roots of unity. Wrapping this support in an arbitrary spectral construction therefore falls under the line mandate's warning against spectral repackaging unless the kernel contributes a mathematically forced mechanism that survives removal of the support tautology.

This closes the support-only version of the most immediate non-scalar escape from PC-386/PC-387:

\[
\text{primorial primitive shell}
\longrightarrow
\text{growing boundary support}
\longrightarrow
\text{prime/rough-number detector}
\tag{16}
\]

is classical sieve structure. It does **not** close non-scalar boundary operators themselves. In particular, a forced operator whose spectrum or cross-scale covariance uses prime-gap interactions in a way not determined by support selection alone remains a legitimate target, but its mathematical delta must be exhibited independently.

## 5. Prior-art and novelty audit

The arithmetic substance of (3), (5), and (11) is classical sieve theory. Buchstab's identity is the standard recursion for sifted sets, and Buchstab's function governs the asymptotic density of integers free of small prime factors. A modern explicit reference is Kai (Steve) Fan, **Numerically explicit estimates for the distribution of rough numbers**, *Journal of Number Theory* 260 (2024), 120–150, DOI `10.1016/j.jnt.2024.01.008`, arXiv:2306.03347. The classical sieve reference is H. Halberstam and H.-E. Richert, **Sieve Methods**, Academic Press (1974).

The exact prime-only threshold `H<p_+(x)^2` is an elementary consequence of the least-prime-factor definition of rough numbers, not a new theorem of sieve theory. Likewise, reduced residues modulo a primorial are the standard primorial wheel. The line-specific contribution here is only the exact identification of the **prime-circle primitive boundary support and its geometric scale thresholds** with these classical objects, and the resulting no-go boundary for attributing support-level prime detection to the geometry.

No novel zeta or RH mechanism is claimed. The novelty audit therefore classifies this result as a `PRIOR-ART-CLASSICALIZATION` with a useful prime-circle consequence: retaining a mesoscopic boundary point cloud preserves arithmetic information that scalar traces can lose, but that information begins as the already-classical rough-number sieve.

## 6. Boundary and falsification checks

The argument depends on primorial shells `N_x`; it does not claim that an arbitrary squarefree shell has the same one-parameter rough-number description. It also concerns boundary windows in the exponent coordinate anchored at `1`; different nonlocal selections may retain different arithmetic. Finally, equations (13)–(15) do not classify spectra of all forced kernels. They isolate the support contribution from the interaction contribution.

The key exact statements are falsifiable by direct finite checks: for each `x`, enumerate `1\le a<p_+(x)^2`, test `(a,N_x)=1`, and compare with `1` plus primes `p>x`; the first non-prime survivor must be `p_+(x)^2`. A counterexample would invalidate the finding immediately. The proof above shows none can occur.

## Consequence for the research line

PC-386/PC-387 showed that scalar primitive-shell chord observables either retain a classical coprimality sieve or wash it out at leading order. PC-388 shows that avoiding scalarization by retaining a growing primorial boundary **does** preserve fine arithmetic, but at support level it preserves exactly the standard rough-number wheel. The next meaningful tests should therefore keep non-scalar structure while explicitly subtracting this tautological support contribution—for example through forced cross-level transport or interaction invariants whose content cannot be reconstructed from the rough-number index set alone.