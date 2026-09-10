# WP-233 — Adjacent Gamma jump density samples the Bost–Connes Weil ray, but its positive completion is the divergent diagonal

**Status:** `EXACT-DERIVED + RIEMANN-GAMMA-RECURRENCE + MARKOV-POSITIVE-JUMP-DIFFERENCE + BOST-CONNES-CRITICAL-HALF-DENSITY + EXACT-PRIME-RAY-SAMPLING + SOURCE-LOG-SCALE + POSITIVE-JUMP-COMPLETION + DIVERGENT-DIAGONAL + DIVISOR-L1-VERSUS-ARCHIMEDEAN-LOG-MISMATCH + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

`WP-117` gives the Prime-Circle-selected Riemann Gamma variation an independent Markov positivity theorem, while `WP-216` shows that the Bost–Connes critical KMS geometry independently forces the finite-place half-density `p^{-k/2}` but places the finite Weil ray in the indefinite defect `log p (I-G_p)`. There is an exact bridge between these two structures which is stronger than a numerical resemblance.

For

\[
h_a(u)=\operatorname{Re}\psi(a+iu)-\psi(a),
\]

the one-step Gamma recurrence implies

\[
\boxed{
 h_a(u)-h_{a+1}(u)
 =\int_0^\infty (1-\cos ux)e^{-ax}\,dx
 =\frac{u^2}{a(a^2+u^2)}.
}
\tag{1}
\]

At the Riemann value selected in `WP-117`, `a=1/4` and `u=t/2`, this becomes

\[
\boxed{
D_\Gamma(t)
:=h_{1/4}(t/2)-h_{5/4}(t/2)
=\int_{\mathbb R}(1-\cos tx)e^{-|x|/2}\,dx
=\frac{16t^2}{1+4t^2}.
}
\tag{2}
\]

Thus a canonical adjacent Gamma difference is itself a positive symmetric jump symbol, with Lévy density

\[
\boxed{J_\infty(x)=e^{-|x|/2}.}
\tag{3}
\]

Now sample that density on the source energies of one Bost–Connes prime ray. For `ell_p=log p`,

\[
\boxed{
J_\infty(k\ell_p)
=e^{-k\log p/2}
=p^{-k/2}.
}
\tag{4}
\]

Multiplying by the same source time-generator scale `ell_p` from `WP-216` gives exactly the critical finite Weil magnitude

\[
\boxed{
\ell_p J_\infty(k\ell_p)
=\frac{\log p}{p^{k/2}}.
}
\tag{5}
\]

This is not enough to prove Weil positivity. In fact, applying the independent jump-energy theorem to the sampled density reconstructs **exactly the positive diagonal completion already known to be missing from the finite Weil block**. On the bilateral exponent ray, with shift `U`, put `r=p^{-1/2}` and

\[
L_p
:=\ell_p\sum_{k\ge1}r^k
(2I-U^k-U^{*k})\succeq0.
\tag{6}
\]

The off-diagonal coefficients of `L_p` are the exact finite Weil coefficients `-\ell_p r^k`, while

\[
\boxed{
L_p=W_p+d_p I,
\qquad
W_p=\ell_p(I-G_p),
\qquad
d_p=\frac{2\ell_p r}{1-r}
=\frac{2\log p}{\sqrt p-1}.
}
\tag{7}
\]

The scalar `d_p` is precisely the sharp local diagonal repair identified in `WP-216`. Equation (7) therefore gives that repair a new, independently selected provenance: it is the total discrete jump rate obtained by restricting the adjacent Riemann-Gamma Lévy density to the `p`-power source energies. But exact Weil matching removes this positive diagonal again, returning the indefinite conductor/defect operator of `WP-190` and `WP-216`.

Globally the repair is unusable as an ordinary positive direct sum because

\[
\boxed{
\sum_p d_p
=\sum_p\frac{2\log p}{\sqrt p-1}
=+\infty.
}
\tag{8}
\]

Moreover, the same exponential profile matches the full Bost–Connes Gram only after replacing the single archimedean distance `|log m-log n|` by the weighted divisor `ell^1` distance

\[
d_{\rm div}(m,n)
:=\sum_p |v_p(m)-v_p(n)|\log p
=\log\frac{mn}{\gcd(m,n)^2}.
\tag{9}
\]

Indeed

\[
\boxed{
e^{-d_{\rm div}(m,n)/2}
=\frac{\gcd(m,n)}{\sqrt{mn}}
=G_1(m,n),}
\tag{10}
\]

whereas the one-dimensional real-place kernel gives

\[
K_\infty(m,n)
:=e^{-|\log m-\log n|/2}.
\tag{11}
\]

For positive integers `m,n`,

\[
\boxed{
\frac{K_\infty(m,n)}{G_1(m,n)}
=\frac{\min(m,n)}{\gcd(m,n)}\ge1,
}
\tag{12}
\]

with equality exactly when one of `m,n` divides the other. Hence the Gamma exponential profile agrees with the Bost–Connes geometry on every divisibility chain, in particular on every single-prime ray, but a single archimedean log coordinate loses the opposing prime valuations as soon as incomparable mixed-prime directions appear. Recovering the full Bost–Connes Gram requires the product/divisor `ell^1` geometry itself, not one real-place distance.

The result therefore sharpens the finite–archimedean boundary in two directions. First, the Riemann Gamma channel does contain a source-natural positive jump profile whose samples are exactly the critical finite-prime magnitudes. Second, using that profile in the ordinary positive way lands exactly in the already-closed passive-jump/positive-diagonal class, and its one-dimensional archimedean geometry does not reproduce the mixed-prime Bost–Connes kernel. A viable global mechanism must couple finite and infinite places before this local sampling/direct-sum step, or otherwise change the operator/domain category while proving the final sign independently.

## 1. The adjacent Gamma difference is an exact positive jump symbol

`WP-117` starts from the classical integral representation, valid for `a>0`,

\[
h_a(u)
=\int_0^\infty
(1-\cos ux)
\frac{e^{-ax}}{1-e^{-x}}\,dx.
\tag{13}
\]

Subtract the same expression with `a` replaced by `a+1`. The denominator cancels exactly:

\[
\frac{e^{-ax}-e^{-(a+1)x}}{1-e^{-x}}
=e^{-ax}.
\tag{14}
\]

Therefore

\[
h_a(u)-h_{a+1}(u)
=\int_0^\infty(1-\cos ux)e^{-ax}\,dx.
\tag{15}
\]

The right-hand side is a standard symmetric Lévy–Khintchine symbol. Its symmetric Lévy measure is

\[
\nu_a(dx)=\frac12e^{-a|x|}\,dx,
\tag{16}
\]

so the difference is continuous conditionally negative definite and its translation-invariant Dirichlet form is nonnegative for the ordinary reason that it is an integral of squared increments. No zeta zero, RH assumption, or target-fitted sign is used.

The rational formula follows directly:

\[
\int_0^\infty e^{-ax}\,dx=\frac1a,
\qquad
\int_0^\infty e^{-ax}\cos(ux)\,dx
=\frac{a}{a^2+u^2},
\]

hence

\[
h_a(u)-h_{a+1}(u)
=\frac1a-\frac{a}{a^2+u^2}
=\frac{u^2}{a(a^2+u^2)}.
\tag{17}
\]

For the Riemann normalization `a=1/4`, `u=t/2`, equation (17) is exactly (2). The shift by one is not chosen to fit a prime coefficient: it is the elementary Gamma/digamma recurrence `psi(z+1)=psi(z)+1/z` applied to the already selected `a=1/4` channel.

## 2. The Gamma jump density is exactly the critical Bost–Connes ray profile

The density in (2) is

\[
J_\infty(x)=e^{-|x|/2}.
\tag{18}
\]

The Bost–Connes source time evolution grades `mu_p` by `log p`, so the `k`th repetition has positive energy

\[
E_{p,k}=k\log p.
\tag{19}
\]

Sampling (18) on this source spectrum gives (4) without an adjustable exponent. This is the same half-density which `WP-216` obtains independently by normalizing the critical KMS conditioned vectors. The logarithmic factor is also source-defined there by

\[
\delta(\mu_p)=i(\log p)\mu_p.
\tag{20}
\]

Thus the bridge uses two structures already selected internally by Mathia:

\[
\text{Prime-Circle Riemann Gamma recurrence}
\quad\rightsquigarrow\quad e^{-|x|/2},
\]

and

\[
\text{Bost–Connes critical source spectrum}
\quad\rightsquigarrow\quad x=k\log p,\ \ell_p=\log p.
\]

Their composition gives (5), the exact finite Weil magnitude. This is stronger than observing the same exponent `1/2` in two formulas: the full repetition law is obtained by evaluating one canonical archimedean jump density on one canonical finite source spectrum.

## 3. Independent positivity forces exactly the missing diagonal

Let `U` be the bilateral unit shift on `ell^2(Z)`. Restricting the Gamma density to the lattice `k ell_p`, `k in Z`, and multiplying by the source logarithmic scale gives symmetric jump rates

\[
c_{p,k}=\ell_p r^{|k|},
\qquad r=p^{-1/2}.
\tag{21}
\]

The associated graph/Dirichlet Laplacian is (6). For a finitely supported vector `f`,

\[
\langle f,L_pf\rangle
=\ell_p\sum_{k\ge1}r^k\|U^kf-f\|^2
\ge0.
\tag{22}
\]

Its Fourier symbol is

\[
\lambda_p(\theta)
=2\ell_p\sum_{k\ge1}r^k(1-\cos k\theta)
\ge0.
\tag{23}
\]

On the same bilateral normalization, the Bost–Connes/Poisson Gram has symbol

\[
P_r(\theta)=1+2\sum_{k\ge1}r^k\cos k\theta,
\tag{24}
\]

so the finite Weil defect is

\[
W_p
=\ell_p(I-G_p)
=-\ell_p\sum_{k\ge1}r^k(U^k+U^{*k}).
\tag{25}
\]

Comparing (6) and (25) gives (7), because

\[
2\ell_p\sum_{k\ge1}r^k
=\frac{2\ell_p r}{1-r}.
\tag{26}
\]

This is also the minimal scalar diagonal needed to lift the minimum of the Poisson-defect symbol to zero. Hence the Gamma-derived jump theorem does not merely add *some* positive normalization: it reproduces the exact sharp repair already forced by the finite operator.

That coincidence is the decisive part of the finding. The archimedean Gamma recurrence does not cancel or geometrically reinterpret the troublesome finite diagonal. Its ordinary positive use **is** that diagonal completion.

## 4. The all-prime direct sum diverges at the exact critical normalization

From (7),

\[
d_p=\frac{2\log p}{\sqrt p-1}
>\frac{2\log p}{\sqrt p}.
\tag{27}
\]

The prime sum on the right diverges, so (8) follows. In particular a direct sum of the independently positive prime-ray jump Laplacians carries infinite diagonal self-energy.

This is consistent with, but more source-specific than, `WP-009`. That finding starts with the already extracted critical prime-power measure and proves that treating those atoms as passive jump conductances gives infinite energy on every nonzero compactly supported Weil test and differs from the finite Weil form by a divergent positive diagonal. The present calculation explains why the same failed conductance law is reached from the **independently selected Riemann Gamma channel itself**: the one-step Gamma recurrence has exactly the exponential density whose Bost–Connes samples are those conductances.

Thus Gamma does not supply the missing counterterm by this route. It canonically reproduces the positive term that must be subtracted to recover the signed finite Weil block.

## 5. The full Gram exposes a finite-versus-archimedean metric mismatch

There is a second obstruction that is invisible on one prime ray. The exponential kernel

\[
k(x,y)=e^{-|x-y|/2}
\tag{28}
\]

is positive definite on the real line; for example, its Fourier transform is a positive multiple of

\[
\frac1{\xi^2+1/4}.
\tag{29}
\]

It is the standard stationary Ornstein–Uhlenbeck/exponential covariance kernel. If the real-place logarithm were the common global coordinate, one would obtain (11).

But `WP-216` gives the exact Bost–Connes critical Gram (10). Writing prime valuations explicitly shows that its metric exponent is not the scalar logarithmic distance but the divisor `ell^1` distance (9):

\[
G_1(m,n)
=\prod_p e^{-\frac12|v_p(m)-v_p(n)|\log p}.
\tag{30}
\]

For `n>=m`, equation (11) gives `K_infty(m,n)=sqrt(m/n)`, while (10) gives `G_1(m,n)=gcd(m,n)/sqrt(mn)`. Their ratio is

\[
\frac{\sqrt{m/n}}{\gcd(m,n)/\sqrt{mn}}
=\frac{m}{\gcd(m,n)},
\tag{31}
\]

which proves (12); the case `m>=n` is symmetric.

Therefore the match is exact not only on prime rays but on every divisibility chain, and fails exactly when the two integers are incomparable in divisibility. For the first mixed-prime example,

\[
G_1(2,3)=\frac1{\sqrt6},
\qquad
K_\infty(2,3)=\sqrt{\frac23}=2G_1(2,3).
\tag{32}
\]

A single real logarithmic coordinate allows positive and negative prime-valuation changes to cancel before absolute value is taken. The Bost–Connes Gram takes absolute value prime by prime first and therefore remembers the full divisor incidence. The two geometries coincide precisely where no such cancellation is possible.

This supplies a concrete mixed-prime falsification of the idea that the Gamma exponential kernel itself is already the global Bost–Connes completion.

## 6. Aggressive controls and exact scope

**Could the positive Gamma jump symbol itself be called the Weil form?** No. Its discrete prime-ray restriction is `L_p`, not `W_p`; equation (7) shows the exact extra diagonal. Removing the diagonal is the order-destroying step already exposed in `WP-190` and `WP-216`.

**Could the extra diagonal be the archimedean counterterm?** Not by direct summation. It is prime dependent, additive over the primes, and diverges as (8). The actual Gamma/polar part of the Weil explicit formula is one global archimedean distribution, not a separate `d_p I` attached to every finite place. Identifying them would require a new renormalized/global theorem, not the jump positivity in (22).

**Could one use only the one-dimensional Gamma kernel `K_infty` and avoid the product geometry?** Equation (12) rules this out once mixed-prime incomparable states are present. It agrees with `G_1` only on divisibility chains.

**Could one instead use the divisor `ell^1` metric?** Yes, and equation (10) does exactly that. But this reconstructs the already positive Bost–Connes/Poisson Gram, whose Weil defect remains indefinite. It is finite-place product geometry, not a finite–archimedean coupling that produces Gamma and polar terms.

**Could a shared nonseparable continuum sector avoid the divergent direct-sum diagonal?** This finding does not rule that out. A single continuum Gamma geometry coupled to all prime source modes before restriction could create correlations absent from the independent ray sum. Such a construction must derive the coupling and its domain from the source, recover the exact explicit-formula decomposition, and prove the final sign without target-dependent sampling or zero data.

**Could a distributional or renormalized restriction of `J_infty` to the Bost–Connes spectrum work?** Also not excluded. But ordinary point sampling followed by positive jump assembly is fully classified by (6)--(8), and arbitrary subtraction of its divergent diagonal is exactly the kind of regularization the research mandate excludes unless independently forced.

**Does this depend on primality?** The local mechanism does not. For any free commutative monoid with generator energies `ell_j>0`, the same density gives `e^{-k ell_j/2}`, and the product kernel is `exp[-(1/2) sum_j |alpha_j-beta_j| ell_j]`. The one-ray sampling and its positive jump completion therefore survive generalized-prime controls. Riemann specificity comes only from independently selecting the actual prime energies and the Riemann Gamma channel; the positivity theorem itself is universal.

## 7. Prior art and novelty boundary

No historical novelty is claimed for the digamma recurrence, its integral representation, Lévy–Khintchine/Schoenberg theory, the exponential/Ornstein–Uhlenbeck covariance kernel, GCD-kernel positivity, Bost–Connes dynamics, Burnol's local scattering, or Weil's explicit formula.

The two special-function identities used above are standard and are recorded in NIST DLMF §5.5(i), Eq. 5.5.2,

`psi(z+1)=psi(z)+1/z`,

and DLMF §5.9(ii), Eq. 5.9.12, the integral representation of `psi` for `Re z>0`. The exponential kernel is a classical positive-definite stationary covariance, equivalently an immediate Bochner-theorem consequence of its positive Cauchy Fourier density. The literature audit also rechecked Connes and Consani, *BC-system, absolute cyclotomy and the quantized calculus*, EMS Surveys in Mathematical Sciences 9, DOI `10.4171/EMSS/64`, which explicitly places the BC system, trace formulas and Weil positivity in one classical research landscape. No source found in the bounded audit was used to claim the exact bridge (2)--(7) as a new theorem of the literature.

Internal prior art is especially important here. `WP-190` already identifies the positive finite Poisson ray with Burnol's p-adic time-delay operator and the signed finite Weil block with its conductor defect. `WP-117` already derives the Riemann Gamma Markov density, `WP-216` derives the source-forced Bost–Connes critical Gram and its sharp diagonal repair, and `WP-009` already closes the direct passive-jump interpretation of the critical prime-power measure.

The durable Mathia-specific delta is therefore narrow but exact: **the canonical one-step recurrence of the independently selected Riemann Gamma Markov channel has exponential jump density `e^{-|x|/2}`; sampling that density on the independently selected Bost–Connes prime-power energies gives the exact finite Weil half-density, and the positive jump theorem then reproduces exactly the sharp local diagonal repair whose all-prime sum diverges.** In addition, the full-kernel calculation (12) identifies precisely why the apparent archimedean match stops at divisibility chains: the Bost–Connes geometry uses divisor `ell^1` distance, not scalar real logarithmic distance.

This is a bridge-and-obstruction result, not a claim that Mathia has found global Weil positivity.

## 8. Consequence for the live research frontier

The finite and archimedean structures are now closer than `WP-117` and `WP-216` separately showed. The same exponential profile occurs in two independently selected places:

\[
\text{Riemann Gamma adjacent Markov difference}
\longrightarrow e^{-|x|/2},
\qquad
\text{BC critical prime energy }k\log p
\longrightarrow p^{-k/2}.
\tag{33}
\]

But the independent positivity theorem associated with that profile yields

\[
\boxed{
\text{positive jump completion}
=\text{finite Weil defect}
+\text{divergent positive diagonal}.
}
\tag{34}
\]

Meanwhile the one-dimensional archimedean distance reconstructs the finite Gram only along divisor-comparable states. Passing to the full finite arithmetic geometry requires the product `ell^1` metric, after which one is back at the Bost–Connes Poisson Gram and its indefinite Weil defect.

The surviving target is therefore more specific. A successful construction cannot merely sample the Gamma jump density independently on each prime ray, direct-sum the resulting positive Laplacians, or identify the real logarithmic OU kernel with the full finite Gram. It must create a **single nonseparable finite–archimedean incidence before positivity is read out**, so that the diagonal/global counterterms are produced by the same geometry rather than subtracted after an infinite positive completion. This leaves active the category changes already isolated by the branch — singular/domain-sensitive correspondences, noncommuting cross-representation couplings, genuinely global compressions/quotients, or cohomological/intersection pairings with an independent sign theorem — while closing this particularly natural Gamma-to-BC passive-jump bridge.

## Dependencies

- `research/weil_positivity/findings/WP-009-prime-lattice-weil-weights-fail-passive-jump-energy.md`
- `research/weil_positivity/findings/WP-117-riemann-gamma-digamma-variation-is-markov-positive-but-critical-prime-coupling-diverges.md`
- `research/weil_positivity/findings/WP-190-prime-circle-poisson-ray-is-burnol-p-adic-time-delay-and-weil-block-is-its-conductor-defect.md`
- `research/weil_positivity/findings/WP-216-bost-connes-critical-conditioning-forces-poisson-gcd-gram-but-weil-ray-is-indefinite-defect.md`
- `research/weil_positivity/findings/WP-232-bost-connes-poisson-whitening-is-an-indefinite-jacobi-normal-form.md`
- `research/weil_positivity/SOURCES.md`

## Bottom line

The Riemann Gamma recurrence does provide an exact and independently positive bridge to the critical finite coefficients: its adjacent Markov difference has jump density `e^{-|x|/2}`, and evaluating that density at `k log p` gives `p^{-k/2}` exactly. With the Bost–Connes logarithmic source scale, the resulting jump rates are `log p / p^{k/2}`.

But ordinary jump positivity then forces precisely the diagonal `2 log p/(sqrt p-1)` that the finite Weil block omits, and those diagonals diverge when summed over primes. At the full-kernel level the same exponential profile agrees with the Bost–Connes Gram only on divisibility chains; mixed-prime states require the divisor `ell^1` product geometry rather than the single archimedean logarithmic coordinate. The bridge is exact, but it lands exactly on a previously identified obstruction rather than yielding a global Weil-positive geometry.