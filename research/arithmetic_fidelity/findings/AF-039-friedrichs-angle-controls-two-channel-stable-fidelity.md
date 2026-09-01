# AF-039 — Friedrichs angle controls two-channel stable fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `STRUCTURAL-CLASSIFICATION`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `H` be a real or complex Hilbert space and let `M,N\subset H` be closed subspaces with orthogonal projections `P,Q`. Put

\[
K=M\cap N,
\qquad
M_0=M\ominus K,
\qquad
N_0=N\ominus K,
\]

and let

\[
W=\overline{M+N},
\qquad
W_0=W\ominus K.
\]

The two retained channel observations are

\[
\mathcal A:W\to M\oplus N,
\qquad
\mathcal A h=(Ph,Qh),
\]

with fusion operator

\[
S=\mathcal A^*\mathcal A=P+Q.
\]

Define the Friedrichs cosine

\[
c(M,N)
=
\sup\left\{
|\langle m,n\rangle|:
 m\in M_0,\ n\in N_0,\ \|m\|=\|n\|=1
\right\},
\]

with the usual convention `c(M,N)=0` if one reduced subspace is zero. Then:

1. **Exact zero-noise fidelity is automatic on the generated support.**
   \[
   \boxed{\ker(\mathcal A|_W)=\{0\}.}
   \]
   Equivalently, the support projection of `S` is `P_W`. Thus the complete pair `(Ph,Qh)` determines `h\in W` exactly even when `M+N` is not closed.

2. **Stable fidelity has a strictly stronger criterion.** On the reduced generated space `W_0`,
   \[
   \boxed{
   \inf_{\substack{h\in W_0\\ \|h\|=1}}
   \left(\|Ph\|^2+\|Qh\|^2\right)
   =1-c(M,N).
   }
   \]
   On the common part `K`, `S=2I`. Hence a positive lower fusion-frame bound on all of `W` exists exactly when
   \[
   \boxed{c(M,N)<1.}
   \]

3. **The same condition is the closed-sum condition.** For closed subspaces,
   \[
   \boxed{
   c(M,N)<1
   \iff
   M+N\text{ is closed}
   \iff
   \mathcal A|_W\text{ is bounded below}.
   }
   \]
   Therefore exact recoverability and continuously/Lipschitz-stable recoverability are genuinely different compression properties.

4. **When `c(M,N)=1`, there are asymptotic same-destination collisions without an exact collision.** There exist unit vectors `h_j\in W_0` such that
   \[
   \boxed{
   \|Ph_j\|^2+\|Qh_j\|^2\longrightarrow0,
   }
   \]
   even though no nonzero `h\in W` satisfies `Ph=Qh=0`. The unique inverse decoder on `\operatorname{Ran}\mathcal A` therefore exists algebraically but is unbounded and discontinuous at the origin.

5. **Finite-scale stability need not survive a limit.** There are increasing finite-dimensional two-channel systems for which every truncation is exactly and stably recoverable, while their optimal lower bounds tend to zero and the Hilbert-space limit is exact but unstable. Thus
   \[
   \boxed{
   \text{stable at every finite scale}
   \not\Rightarrow
   \text{uniformly stable in the limit}.
   }
   \]

The reusable Arithmetic Fidelity conclusion is:

\[
\boxed{
\text{support fidelity asks whether information is annihilated; stable fidelity asks whether surviving information stays uniformly separated from annihilation.}
}
\]

For asymptotic, thermodynamic, continuum, or infinite-dimensional compression arguments, pointwise finite-stage injectivity is therefore insufficient. A uniform lower spectral bound is an additional gate.

## Derivation

### Exact support fidelity

If `h\in W` and

\[
Ph=0,
\qquad
Qh=0,
\]

then

\[
h\in M^\perp\cap N^\perp=(M+N)^\perp=W^\perp.
\]

Since also `h\in W`, it follows that `h=0`. Hence `\mathcal A|_W` is injective for every pair of closed subspaces.

Moreover

\[
\langle Sh,h\rangle
=
\langle Ph,h\rangle+\langle Qh,h\rangle
=
\|Ph\|^2+\|Qh\|^2,
\]

so

\[
\ker S=M^\perp\cap N^\perp=W^\perp.
\]

For a bounded positive self-adjoint operator,

\[
\overline{\operatorname{Ran}S}=(\ker S)^\perp=W,
\]

and therefore the support projection of `S` is exactly `P_W`. This is the two-channel specialization of AF-038's support theorem.

### The reduced synthesis operator exposes the sharp stability constant

On the reduced spaces define

\[
B:M_0\oplus N_0\to W_0,
\qquad
B(m,n)=m+n.
\]

Because `M_0\cap N_0=\{0\}`, the map `B` is injective. Its adjoint is

\[
B^*h=(Ph,Qh),
\qquad h\in W_0,
\]

and

\[
BB^*=S|_{W_0}.
\]

For `(m,n)\in M_0\oplus N_0`,

\[
\begin{aligned}
\|B(m,n)\|^2
&=\|m\|^2+\|n\|^2+2\operatorname{Re}\langle m,n\rangle\\
&\ge
\|m\|^2+\|n\|^2-2c(M,N)\|m\|\|n\|\\
&\ge
(1-c(M,N))(\|m\|^2+\|n\|^2).
\end{aligned}
\]

The constant is sharp: by the definition of `c(M,N)`, choose unit reduced vectors whose inner products approach the supremum in modulus and rotate the phase/sign of one vector so that the real part approaches `-c(M,N)`. For those pairs,

\[
\|m+n\|^2\longrightarrow2(1-c(M,N)).
\]

Thus

\[
\inf\sigma(B^*B)=1-c(M,N).
\]

The nonzero spectra of `B^*B` and `BB^*` agree, with zero entering the spectrum in the non-closed-range case. Consequently

\[
\inf\sigma(S|_{W_0})=1-c(M,N),
\]

which is exactly

\[
\inf_{\|h\|=1,\ h\in W_0}
\left(\|Ph\|^2+\|Qh\|^2\right)
=1-c(M,N).
\]

On `K`, both projections are the identity, so `S=2I`. The common information is therefore maximally well conditioned; all instability lives in the reduced relative position of the channels.

### Closed sum, lower frame bound, and decoder continuity are the same boundary

The classical Friedrichs-angle theorem gives

\[
M+N\text{ closed}
\iff
c(M,N)<1.
\]

The same equivalence also follows directly from the synthesis map. Since `B` is a bounded injective operator with range `M_0+N_0`, its range is closed exactly when `B` is bounded below. The sharp lower bound above is positive exactly when `c(M,N)<1`.

Because `\mathcal A=B^*` on `W_0`, the same positive spectral gap is the lower analysis bound

\[
\|\mathcal Ah\|^2
=\|Ph\|^2+\|Qh\|^2
\ge
(1-c(M,N))\|h\|^2.
\]

When this holds, the inverse

\[
\mathcal A^{-1}:\operatorname{Ran}\mathcal A\to W
\]

is bounded, with reduced Lipschitz constant at most

\[
(1-c(M,N))^{-1/2}.
\]

When `c(M,N)=1`, the lower bound is zero. Injectivity remains true, but there are unit vectors with observed norm tending to zero; hence the algebraic inverse cannot be continuous.

This is a strict strengthening of a zero-error fiber audit. The compression has no exact nontrivial fiber on `W`, yet arbitrarily small perturbations of retained data can correspond to order-one changes upstream.

## Explicit asymptotic control: stable truncations with an unstable limit

Let

\[
H_0=\ell^2(\mathbb N),
\qquad
H=H_0\oplus H_0,
\]

and define the bounded injective diagonal operator

\[
De_k=\frac1k e_k.
\]

Its range is dense but not closed. Set

\[
M=H_0\oplus\{0\},
\qquad
N=\operatorname{graph}(D)
=\{(x,Dx):x\in H_0\}.
\]

Both `M` and `N` are closed and

\[
M\cap N=\{0\}.
\]

Their algebraic sum is

\[
M+N=H_0\oplus\operatorname{Ran}D,
\]

which is dense but not closed in `H`. Thus

\[
W=\overline{M+N}=H,
\qquad
c(M,N)=1.
\]

The angle collapse can be seen coordinatewise. The line in `M` generated by `(e_k,0)` and the line in `N` generated by `(e_k,k^{-1}e_k)` have cosine

\[
c_k
=
\frac{1}{\sqrt{1+k^{-2}}}
\longrightarrow1.
\]

On their two-dimensional coordinate block, the two-projection operator `P+Q` has eigenvalues

\[
1\pm c_k.
\]

Hence its smallest positive eigenvalue is

\[
\alpha_k=1-c_k
=1-\frac1{\sqrt{1+k^{-2}}}
\sim\frac1{2k^2}.
\]

Now truncate to

\[
H^{(n)}
=\operatorname{span}\{e_1,\ldots,e_n\}
\oplus
\operatorname{span}\{e_1,\ldots,e_n\}
\]

with the corresponding `M^{(n)}` and `N^{(n)}`. Every finite truncation has

\[
c(M^{(n)},N^{(n)})
=
\frac1{\sqrt{1+n^{-2}}}<1,
\]

and is therefore stably recoverable. Its optimal lower bound is

\[
\boxed{
\alpha_n
=1-\frac1{\sqrt{1+n^{-2}}}
\sim\frac1{2n^2}.
}
\]

Nevertheless

\[
\alpha_n\to0,
\]

and the infinite system has no positive lower bound. This is an exact matched control for any argument that infers stable infinite-scale fidelity merely from exact or well-posed finite truncations.

The phenomenon is not numerical pathology: the limiting compression is still injective on its generated support. What fails is **uniform separation of distinct upstream states in the destination norm**.

## Destination-category boundary

The theorem applies when the destination really retains the two Hilbert-space channel projections

\[
(Ph,Qh)
\]

or information exactly equivalent to them. It does not license replacing scalar summaries, spectra, traces, marginal moments, or other already-compressed outputs by their upstream projection subspaces.

For the channel setting of AF-038, one may take

\[
M=L^2(\mathcal F_1),
\qquad
N=L^2(\mathcal F_2),
\]

provided the destination makes the corresponding conditional-expectation vectors available. Then the Friedrichs cosine measures the reduced overlap between the two information subspaces after their common part is removed. If the common `\sigma`-field is trivial, this is the familiar maximal-correlation geometry of the two channels. A value approaching one means that the channels contain nearly coincident nonconstant directions even when they share no exact nonconstant direction.

This distinction is essential for Arithmetic Fidelity:

\[
\text{same support}
\quad\not\Rightarrow\quad
\text{same conditioning}.
\]

A later nonlinear operation cannot repair an arbitrarily ill-conditioned inverse unless it receives additional information not present in the declared destination or exploits a separately proved restriction on the admissible source class.

## Prior art and novelty assessment

The mathematical ingredients are classical, and no novelty is claimed for the Friedrichs angle, two-projection canonical forms, closed-sum criteria, or frame lower bounds.

- P. R. Halmos, **“Two Subspaces,”** *Transactions of the American Mathematical Society* 144 (1969), 381–389, DOI `10.1090/S0002-9947-1969-0251519-5`. Role: canonical two-subspace/two-projection decomposition; in the generic part, the spectral geometry of `P+Q` is controlled by the relative-angle operator.
- Frank Deutsch, **“The Angle Between Subspaces of a Hilbert Space,”** in *Approximation Theory, Wavelets and Applications*, NATO ASI Series C 454, Kluwer (1995), 107–130, DOI `10.1007/978-94-015-8577-4_7`. Role: expository source for Friedrichs/Dixmier angles and their operator-theoretic applications.
- Irwin E. Schochetman, Robert L. Smith, and Sze-Kai Tsui, **“On the closure of the sum of closed subspaces,”** *International Journal of Mathematics and Mathematical Sciences* 26(5) (2001), 257–267, DOI `10.1155/S0161171201005324`. Role: explicit closed-sum/angle equivalences for Hilbert subspaces.
- Albrecht Böttcher and Ilya M. Spitkovsky, **“A gentle guide to the basics of two projections theory,”** *Linear Algebra and its Applications* 432(6) (2010), 1412–1459, DOI `10.1016/j.laa.2009.11.002`. Role: modern systematic account of the operator and spectral structure of pairs of orthogonal projections.
- The fusion-frame background already audited in AF-038 supplies the established language for lower frame bounds and stable reconstruction from subspaces.

The Arithmetic Fidelity contribution is therefore not a new angle theorem. It is the exact **compression-boundary organization** relative to AF-038: support of the fusion operator classifies zero-noise survival, while the bottom of its positive spectrum classifies stability. In the two-channel case the latter has the sharp closed form `1-c(M,N)`, and the diagonal-graph example shows that finite-stage stability without a uniform angle gap can disappear completely in an infinite/asymptotic limit.

## Boundaries and failure modes

- The sharp scalar `1-c(M,N)` is a two-subspace result on the reduced space. For three or more channels, one must analyze the actual fusion operator or an appropriate multi-subspace angle; pairwise angle bounds alone need not determine the full lower spectrum.
- The common intersection `K` must be removed when defining the Friedrichs angle. Directions in `K` are not an instability: they are observed identically by both channels and have fusion eigenvalue `2`.
- Exact injectivity here is only on `W=\overline{M+N}`. Directions in `W^\perp` were never generated by the declared channels and are correctly annihilated.
- A positive lower bound is topology- and norm-dependent. Changing the destination norm can change quantitative conditioning even when the exact fiber relation is unchanged; any alternative norm must be independently justified by the actual compression.
- Finite-dimensionality automatically makes an injective linear compression bounded below, so finite examples cannot by themselves falsify the infinite-dimensional stability problem. The relevant asymptotic question is whether the lower bound stays uniformly away from zero.
- The graph example is a structural control, not an arithmetic model. Applying the theorem to primes or an explicit-formula representation requires identifying the actual retained Hilbert subspaces and proving that their projection data factor through the proposed destination.

## Consequence for the current Arithmetic Fidelity frontier

AF-038 ended with a distinction between exact support recovery and a fusion-frame lower bound for arbitrary dependent channel families. AF-039 makes that distinction sharp in the first nontrivial case and adds an asymptotic no-go:

\[
\boxed{
\text{before passing a faithful finite-scale construction to a limit, audit the uniform bottom of the retained fusion spectrum.}
}
\]

For a proposed arithmetic or RH compression represented by increasing finite-dimensional approximants, the next valid stability claim must therefore exhibit one of two things:

1. a source-independent or arithmetic-forced lower bound
   \[
   \inf_n \alpha_n>0,
   \]
   where `\alpha_n` is the smallest positive fusion eigenvalue on the relevant discriminator space; or
2. an independently justified source restriction showing that the discriminator never approaches the small-spectrum directions even if the ambient lower bound collapses.

Without one of those gates, exact finite-scale separation can coexist with arbitrarily bad conditioning and carries no stable infinite-scale recovery conclusion.