# AF-272 — Finite prime-power prefixes detect bounded quotient divisor complexity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SOURCE`, `PERIODIC-DIVISOR`, `FINITE-MOMENT-RECOVERY`, `VANDERMONDE`, `STABILITY-BOUNDARY`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-270 shows that exact Bohr recurrence and the correct rational-prime-power frequency ray do not determine critical-line geometry: a periodic infinite zero transport can remain on one ray `p^k` while changing only the coefficient law. For rational periodic controls, however, a bounded number of **distinct signed divisor nodes in the quotient after cancellation** gives a finite certificate.

Fix a rational prime `p`, set

\[
\lambda:=\log p,
\qquad z:=p^{-s},
\qquad L:=\frac{2\pi}{\lambda},
\]

and consider a rational periodic quotient

\[
Q(s)=Cz^\nu\prod_{j=1}^{R}(1-\alpha_j z)^{m_j},
\]

where `C != 0`, `nu in Z`, the `alpha_j in C^*` are pairwise distinct, and the nonzero integers `m_j` are signed zero/pole multiplicities **after all common divisor nodes have been cancelled**. On every right half-plane on which `|alpha_j p^{-s}|<1`,

\[
\frac{Q'}{Q}(s)
=-\nu\lambda
+\lambda\sum_{k\ge1}q_k p^{-ks},
\qquad
q_k=\sum_{j=1}^{R}m_j\alpha_j^k.
\tag{1}
\]

Then:

1. **Quotient-complexity detection.** If `q_1=...=q_R=0`, then every `m_j=0`. Thus a nontrivial quotient with at most `R` distinct nonconstant signed divisor nodes must change at least one of the first `R` coefficients on the prime-power ray.

2. **Pairwise controls pay the union complexity.** If two rational periodic controls each have at most `r` distinct nonconstant divisor nodes, their quotient has at most `2r` distinct signed divisor nodes after cancellation. Therefore agreement of their first `2r` nonconstant source coefficients forces their nonconstant divisors to agree. The shorter `r`-coefficient conclusion is false in general when `r` bounds each control separately rather than the quotient.

3. **No universal finite prefix without a quotient-complexity bound.** For every `K>=1` and `A in C^*`,

\[
R_{K+1}(z):=1-(Az)^{K+1}
\tag{2}
\]

has `K+1` distinct divisor nodes while its first `K` source coefficients vanish exactly.

4. **Exact fidelity is unstable without geometric control.** Even for quotient complexity two,

\[
Q_\varepsilon(z)=\frac{1-\alpha z}{1-(\alpha+\varepsilon)z}
\tag{3}
\]

has a nontrivial signed divisor for every `epsilon != 0`, while every fixed finite coefficient window tends to zero as `epsilon -> 0`.

5. **Separated compact quotient classes have a quantitative gap.** If additionally

\[
0<a\le |\alpha_j|\le b,
\qquad
|\alpha_i-\alpha_j|\ge\delta>0
\quad(i\ne j),
\]

and `B=max(1,b)`, then

\[
\left(\sum_{k=1}^{R}|q_k|^2\right)^{1/2}
\ge
\frac{a^R\delta^{R(R-1)/2}}
{(RB^R)^{R-1}}.
\tag{4}
\]

The information budget is therefore attached to the **difference object being audited**, not separately to either representation. This distinction is essential: individual complexity bounds combine by union before the Vandermonde certificate can be applied.

## Exact derivation

### 1. Periodic divisor quotients are finite power-sum sources

Because `z=p^{-s}` is invariant under `s -> s+iL`, each factor `(1-alpha_j z)` describes one vertical zero/pole lattice modulo that period. Logarithmic differentiation gives

\[
\frac{d}{ds}\log z^\nu=-\nu\lambda
\]

and, whenever `|alpha_j z|<1`,

\[
\frac{d}{ds}\log(1-\alpha_j z)^{m_j}
=m_j\lambda\sum_{k\ge1}\alpha_j^kz^k.
\]

Summing yields `(1)`. The nonconstant source difference is the power-moment sequence of the finite signed divisor measure

\[
\mu_Q:=\sum_{j=1}^{R}m_j\delta_{\alpha_j}.
\tag{5}
\]

Thus the appropriate complexity is the support cardinality of `mu_Q` **after cancellation**.

### 2. The first `R` vanishing coefficients kill an `R`-node quotient

Let

\[
q=(q_1,\ldots,q_R)^T,
\qquad
m=(m_1,\ldots,m_R)^T,
\]

and set `V_{kj}=alpha_j^k` for `1<=k,j<=R`. Then `q=Vm` and

\[
\det V
=\left(\prod_{j=1}^{R}\alpha_j\right)
\prod_{1\le i<j\le R}(\alpha_j-\alpha_i)
\tag{6}
\]

up to the conventional Vandermonde sign. Every factor is nonzero, so `V` is invertible. Hence `q_1=...=q_R=0` implies `m=0`.

This is a null-detection statement, not a claim that `R` arbitrary moments reconstruct unknown nodes and weights. Classical Prony recovery normally uses a longer window because the node locations are themselves unknown parameters. Here the quotient is already formed, and the question is only whether a signed divisor with at most `R` distinct nodes can be invisible to its first `R` positive power sums.

### 3. Individual control complexity is not quotient complexity

Let two controls have signed divisor measures `mu_1` and `mu_2`, each supported on at most `r` nonzero nodes. Their quotient has signed divisor

\[
\mu_Q=\mu_1-\mu_2,
\]

whose support is contained in `supp(mu_1) union supp(mu_2)`. Therefore

\[
|\operatorname{supp}\mu_Q|\le2r.
\tag{7}
\]

Applying the preceding theorem with `R=2r` proves that equality of the first `2r` source coefficients forces `mu_Q=0`, hence equality of the nonconstant divisors.

The factor two cannot simply be discarded. Already for `r=2`, take

\[
\mu_1=\delta_1+\delta_{-1},
\qquad
\mu_2=2\delta_i-\delta_{2i}.
\tag{8}
\]

Each measure has two distinct nonzero nodes with nonzero integer multiplicities, but

\[
q_1(\mu_1)=0=q_1(\mu_2),
\qquad
q_2(\mu_1)=2=q_2(\mu_2).
\tag{9}
\]

Nevertheless `mu_1-mu_2` is nonzero and has four distinct nodes. Thus the first `r` coefficients do **not** identify two controls merely because each has individual complexity at most `r`. The Vandermonde dimension is controlled by the cancelled quotient support.

This example also separates two tasks that are easy to conflate:

- auditing one already-formed quotient of support size at most `R` needs `R` vanishing moments;
- comparing two independently unknown `r`-node controls has a safe null-detection budget of `2r` moments because the difference may have twice as many nodes.

No claim is made here that `2r` is the minimal pairwise budget in every restricted subclass; extra positivity, common support, known multiplicities, symmetry, or other structure can reduce it.

### 4. Unbounded quotient complexity defeats every fixed prefix

Put `R=K+1` and factor `(2)` over the `R`th roots of unity:

\[
1-(Az)^R
=\prod_{j=0}^{R-1}(1-A\omega_R^jz),
\qquad
\omega_R=e^{2\pi i/R}.
\]

Its logarithmic derivative is

\[
-\lambda z\frac{d}{dz}\log(1-(Az)^R)
=\lambda R\sum_{n\ge1}A^{Rn}z^{Rn}.
\tag{10}
\]

Hence the coefficients of degrees `1,...,R-1` vanish although the quotient has `R` nonconstant divisor nodes. No prefix length independent of quotient complexity can therefore audit all finite rational periodic divisor changes.

### 5. Exact detection can be arbitrarily ill-conditioned

For `(3)`,

\[
q_k(\varepsilon)=\alpha^k-(\alpha+\varepsilon)^k.
\]

For every fixed `K`,

\[
\max_{1\le k\le K}|q_k(\varepsilon)|\to0
\qquad(\varepsilon\to0),
\]

while the signed divisor remains nonzero for every `epsilon != 0`. Exact finite-prefix completeness therefore has no uniform positive robustness modulus over unrestricted node configurations.

Under the radial and separation assumptions in the claim, `(6)` gives

\[
|\det V|\ge a^R\delta^{R(R-1)/2}.
\]

Every entry obeys `|V_{kj}|<=B^R`, so `||V||_2<=||V||_F<=RB^R`. If `sigma_min(V)` is the smallest singular value,

\[
\sigma_{\min}(V)
\ge
\frac{|\det V|}{\|V\|_2^{R-1}}
\ge
\frac{a^R\delta^{R(R-1)/2}}
{(RB^R)^{R-1}}.
\]

Since a nonzero divisor multiplicity vector is integral, `||m||_2>=1`, and `(4)` follows from `q=Vm`. The integer-multiplicity assumption supplies the absolute normalization; arbitrary complex weights would require an explicit weight norm.

## Application to AF-270

For `a != 1/2`, the quotient between the AF-270 periodic controls `H_a/H_{1/2}` is rational in `z=p^{-s}` up to a constant/monomial factor and has exactly three distinct signed divisor nodes

\[
p^a,\qquad p^{1-a},\qquad p^{1/2}
\]

with multiplicities `(+1,+1,-2)`. Its source difference is

\[
q_k=p^{ka}+p^{k(1-a)}-2p^{k/2}.
\tag{11}
\]

Because this is a **three-node quotient**, agreement through the first three prime powers would force the signed divisor to vanish. In this particular family strict convexity is stronger: `q_k>0` for every `k>=1`, so even the first coefficient sees the split.

The corrected lesson from AF-270 is therefore:

\[
\boxed{
\text{bounded quotient divisor complexity}
+\text{matching prefix of that length}
\Longrightarrow
\text{no nonconstant periodic divisor surgery}.
}
\tag{12}
\]

If complexity is known only separately for two controls, one must first bound the complexity of their cancelled quotient; the naive reuse of the individual bound is invalid.

## Prior art and novelty assessment

The finite-moment mathematics is classical. Prony-type methods recover finitely supported exponential sums or atomic measures from moment samples, and the invertibility in `(6)` is the elementary Vandermonde core. Stefan Kunis, Thomas Peter, Tim Roemer, and Ulrich von der Ohe, **“A multivariate generalization of Prony's method,”** *Linear Algebra and its Applications* 490 (2016), 31–47, DOI `10.1016/j.laa.2015.10.023`, situates finite-support parameter reconstruction in that classical lineage.

The conditioning boundary is likewise classical Vandermonde geometry. Fermin S. V. Bazan, **“Conditioning of Rectangular Vandermonde Matrices with Nodes in the Unit Disk,”** *SIAM Journal on Matrix Analysis and Applications* 21(2), 679–693 (2000), DOI `10.1137/S0895479898336021`, studies node-separation-dependent conditioning relevant to exponential parameter recovery.

No novelty is claimed for Prony reconstruction, power-sum identities, Vandermonde invertibility, or separated-node conditioning. The Arithmetic Fidelity specialization is the audit of AF-270's one-prime-ray periodic escape: the support size of the **cancelled divisor quotient** is the finite information budget controlling null detection by prime-power coefficients. The pairwise correction above is structurally important because it identifies exactly where an apparently local complexity assumption can double when two representations are compared.

## Boundaries and failure modes

- The theorem applies to quotients rational in `z=p^{-s}` after constant/monomial ambiguity is separated. General periodic or almost-periodic zero-free factors fall outside this finite-divisor calculation.
- `R` counts distinct signed divisor nodes **of the quotient after cancellation**, not total multiplicity and not automatically the complexity of either input control.
- If each input has at most `r` nodes, `2r` is a safe quotient-support bound, but it is not asserted to be optimal for every structured subclass.
- Exact prefix agreement is not stable without radial compactness and node separation.
- The roots-of-unity escape only proves that fixed prefixes fail for unbounded finite quotient complexity; it does not produce a global zeta-like control satisfying the full Euler coefficient law and completion.
- Different rational-prime rays can couple through a global control. A one-ray theorem does not classify distributed perturbations over infinitely many rays.
- The AF-270 application is a matched-control audit, not an RH implication.

## Consequence for the research line

The useful intermediate layer between frequency support and the full infinite von-Mangoldt coefficient law survives the correction, but its accounting must be performed on the difference object. **Finite source certificates are controlled by cancelled quotient complexity.** Separate bounds on candidate representations combine before the certificate is applied.

This makes the next question more precise: can zeta-specific structure independently bound the effective complexity of an admissible source/divisor **difference**, or force enough shared support/cancellation that the generic union bound is overly pessimistic? A positive theorem would turn a finite prime-power coefficient window into a complete audit for that control class. A negative construction would identify why local source prefixes cannot replace the global Euler law.