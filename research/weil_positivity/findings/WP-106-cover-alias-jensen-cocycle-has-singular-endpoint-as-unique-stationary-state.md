# WP-106 — Cover-alias Jensen defects form a positive cocycle whose unique stationary bulk state is the singular endpoint

**Status:** `EXACT-DERIVED + POSITIVE-COCYCLE + MARKOV-RIGIDITY + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION + NOT-GLOBAL-WEIL`.

`WP-104` and `WP-105` leave a precise loophole.  The weighted Dirichlet geometry has an independently positive operator-Jensen defect under every root-cover refinement, and its bulk alias symbol attains the exact scalar `log n` only at the singular endpoint `phi=0`.  That proves pointwise extremality, but by itself it does not say whether the endpoint was merely selected after seeing the desired scalar or whether the cover geometry forces it dynamically.

It does.  The finite-section Jensen defects form an exact positive semigroup cocycle before any bulk limit is taken.  On the principal-symbol algebra the corresponding alias kernels form a canonical Markov semigroup `P_n`, the Jensen gap is its relative-entropy cocycle, and

\[
\boxed{P_n\ell=\frac1n\ell,\qquad \ell(\phi)=2-2\cos\phi.}
\]

Consequently, for every fixed `n>1`, the dual dynamics `P_n^*` has exactly one stationary probability state,

\[
\boxed{\delta_0,}
\]

and every initial probability state converges weakly to it under repeated refinement.  Equivalently, for every `f\in C(\mathbb T)`,

\[
\boxed{P_n^r f\longrightarrow f(0)}
\]

uniformly.  Under the matched Haar control the statement becomes completely classical: one refinement sends Haar to the Fejer density

\[
\boxed{
F_n(\theta)=\frac1n\left|1+e^{i\theta}+\cdots+e^{i(n-1)\theta}\right|^2
=\frac{\ell(n\theta)}{n\ell(\theta)},
}
\]

and repeated refinement gives the approximate identity `F_{n^r}` concentrating at `0`.

Thus the singular endpoint anchor is not an arbitrary post-hoc state inside the bulk Jensen construction: **semigroup-coherent positive alias refinement forces it as the unique equilibrium and global attractor.**  This is a real strengthening of `WP-105`.  It is nevertheless a negative result for the global Weil objective.  The forced state is precisely the nonclosable endpoint already isolated by `WP-094`--`WP-095`; the dynamics is universal for every integer circle cover; prime-power support still requires an additional Euler-ray/primitive operation, while the canonical Mobius primitive is indefinite by `WP-078`; and no archimedean or polar/global counterterm is produced.

## 1. Exact finite-section operator cocycle

Retain the finite weighted Dirichlet Gram matrices `G_K` and normalized block-replication isometries of `WP-104`,

\[
W_{n,K}e_k=\frac1{\sqrt n}\sum_{r=0}^{n-1}e_{nk+r},
\qquad
W_{n,K}^*G_{nK}W_{n,K}=nG_K.
\tag{1}
\]

Their composition is exact:

\[
\boxed{
W_{n,mK}W_{m,K}=W_{mn,K}.
}
\tag{2}
\]

Indeed, both sides send `e_k` to the normalized sum of the `mn` consecutive basis vectors in the block beginning at `mnk`.

Define the positive operator-Jensen defect

\[
J_{n,K}
:=
\log(nG_K)-W_{n,K}^*\log(G_{nK})W_{n,K}
\succeq0.
\tag{3}
\]

Positivity is exactly the operator concavity of `log` applied to the isometry `W_{n,K}` and the covariance (1), as in `WP-104`.  Expanding (3), using (2), and cancelling the intermediate `log G_{mK}` term gives

\[
\boxed{
J_{mn,K}
=
J_{m,K}
+
W_{m,K}^*J_{n,mK}W_{m,K}.
}
\tag{4}
\]

Every term on the right is positive semidefinite.  Hence the Jensen defects are not merely a collection of positive quantities attached separately to degrees: they form an exact positive cocycle for cover composition.

On a prime-power tower this gives

\[
\boxed{
J_{p^a,K}
=
\sum_{r=0}^{a-1}
W_{p^r,K}^*J_{p,p^rK}W_{p^r,K},
}
\tag{5}
\]

where `W_{p^0,K}=I` and the obvious composed isometries are understood.  Each refinement increment is independently positive.  This identity is finite-dimensional and exact; it is not an asymptotic consequence of the principal symbol.

## 2. The bulk alias weights define a Markov semigroup

For `phi in T=R/(2pi Z)` write

\[
\ell(\phi)=2-2\cos\phi=4\sin^2(\phi/2).
\tag{6}
\]

For degree `n`, the inverse branches of the circle cover `T_n(theta)=n theta` are

\[
\theta_j=\frac{\phi+2\pi j}{n},
\qquad 0\le j<n.
\tag{7}
\]

`WP-105` derives the positive alias weights

\[
w_j^{(n)}(\phi)
=
\frac{\ell(\phi)}{n^2\ell(\theta_j)},
\qquad
\sum_{j=0}^{n-1}w_j^{(n)}(\phi)=1,
\tag{8}
\]

away from `phi=0`, with the continuous endpoint extension

\[
w^{(n)}(0)=(1,0,\ldots,0).
\tag{9}
\]

Define

\[
\boxed{
(P_nf)(\phi)
:=
\sum_{j=0}^{n-1}w_j^{(n)}(\phi)f(\theta_j),
\qquad f\in C(\mathbb T).
}
\tag{10}
\]

Then `P_n` is positive and unital.  More importantly, refinement factors exactly.  If

\[
\alpha_a=\frac{\phi+2\pi a}{m},
\qquad
\beta_{a,b}=\frac{\alpha_a+2\pi b}{n},
\]

then

\[
\begin{aligned}
w_a^{(m)}(\phi)w_b^{(n)}(\alpha_a)
&=
\frac{\ell(\phi)}{m^2\ell(\alpha_a)}
\frac{\ell(\alpha_a)}{n^2\ell(\beta_{a,b})}\\
&=
\frac{\ell(\phi)}{(mn)^2\ell(\beta_{a,b})}.
\end{aligned}
\tag{11}
\]

As `(a,b)` ranges over the two-stage aliases, `beta_{a,b}` ranges once over the `mn` aliases of `phi`.  Therefore

\[
\boxed{
P_mP_n=P_{mn}=P_nP_m.
}
\tag{12}
\]

Thus the bulk compression is a commutative Markov representation of the multiplicative cover semigroup.

## 3. The Jensen gap is exactly the KL cocycle

Let

\[
j_n(\phi)
=
\log\frac{\ell(\phi)}n
-
(P_n\log\ell)(\phi),
\tag{13}
\]

with the continuous extension at `phi=0`.  `WP-105` proves the exact information-theoretic identity

\[
\boxed{
j_n(\phi)
=D_{\rm KL}\!\left(w^{(n)}(\phi)\middle\|u_n\right)
=\sum_jw_j^{(n)}(\phi)\log\bigl(nw_j^{(n)}(\phi)\bigr)
\ge0,
}
\tag{14}
\]

where `u_n` is uniform on the `n` aliases.  It also gives

\[
j_n(0)=\log n,
\qquad
j_n(\phi)<\log n\quad(\phi\ne0).
\tag{15}
\]

Using (12) directly in (13),

\[
\begin{aligned}
j_m+P_mj_n
&=
\log\frac{\ell}{m}-P_m\log\ell
+P_m\!\left(\log\frac{\ell}{n}-P_n\log\ell\right)\\
&=
\log\frac{\ell}{mn}-P_{mn}\log\ell.
\end{aligned}
\]

Hence

\[
\boxed{
j_{mn}=j_m+P_mj_n.}
\tag{16}
\]

Equivalently, (11) factors the `mn`-alias law into a first-stage alias and a conditional second-stage alias, and (16) is precisely the classical chain rule for relative entropy.  No novelty is claimed for the KL chain rule; a standard reference is Cover and Thomas, *Elements of Information Theory*, 2nd ed., Chapter 2, DOI `10.1002/047174882X.ch2`.  The Mathia-specific content is that the principal-symbol limit of the positive operator cocycle (4) realizes that chain rule exactly.

## 4. A strict Lyapunov observable forces the endpoint

The same alias identity used to normalize (8) gives a much stronger rigidity statement.  Multiplying each weight by its alias energy,

\[
\begin{aligned}
(P_n\ell)(\phi)
&=
\sum_{j=0}^{n-1}
\frac{\ell(\phi)}{n^2\ell(\theta_j)}
\ell(\theta_j)\\
&=
\frac{\ell(\phi)}n.
\end{aligned}
\]

Thus

\[
\boxed{P_n\ell=\ell/n.}
\tag{17}
\]

Let `nu` be any probability measure on `T`.  By duality,

\[
\int_{\mathbb T}\ell\,d(P_n^*\nu)
=
\frac1n\int_{\mathbb T}\ell\,d\nu.
\tag{18}
\]

If `nu` is stationary and `n>1`, (18) implies

\[
\int\ell\,d\nu=0.
\]

But `ell>=0` and its zero set on the circle is the single point `0`.  Therefore

\[
\boxed{
P_n^*\nu=\nu
\quad\Longrightarrow\quad
\nu=\delta_0.
}
\tag{19}
\]

The converse is immediate from (9), so `delta_0` is the unique stationary probability state.

The argument gives more than uniqueness.  Iterating (18),

\[
\boxed{
\int\ell\,d((P_n^*)^r\nu)
=n^{-r}\int\ell\,d\nu\longrightarrow0.
}
\tag{20}
\]

Any weak subsequential limit is therefore supported on `ell^{-1}(0)={0}` and must equal `delta_0`.  Compactness of the probability measures on the circle yields the full convergence

\[
\boxed{
(P_n^*)^r\nu\Longrightarrow\delta_0
\qquad(r\to\infty)
}
\tag{21}
\]

for every initial probability state `nu`.

There is also a uniform function-level version.  Since `P_n^r=P_{n^r}` by (12),

\[
(P_{n^r}\ell)(\phi)=\frac{\ell(\phi)}{n^r}\le\frac4{n^r}.
\tag{22}
\]

For every neighborhood `U` of `0`, `ell` has a strictly positive minimum on `T\setminus U`; Markov's inequality applied to the transition probability in (10) therefore bounds the mass outside `U` uniformly in the starting `phi` by `O(n^{-r})`.  Uniform continuity of `f` then gives

\[
\boxed{
\|P_n^rf-f(0)\mathbf1\|_\infty\longrightarrow0
\qquad(f\in C(\mathbb T)).
}
\tag{23}
\]

So the endpoint is a global attractor of the canonical positive alias dynamics, not merely an extremizer of one scalar functional.

## 5. Haar is sent exactly to the Fejer approximate identity

The previous convergence has a sharp matched control.  Let `m` be normalized Haar measure on the circle.  Changing variables `phi=n theta` separately on each inverse branch in (10) gives

\[
\begin{aligned}
\int_{\mathbb T}P_nf(\phi)\,dm(\phi)
&=
\int_{\mathbb T}
f(\theta)
\frac{\ell(n\theta)}{n\ell(\theta)}
\,dm(\theta).
\end{aligned}
\tag{24}
\]

The density is exactly

\[
\boxed{
\frac{\ell(n\theta)}{n\ell(\theta)}
=
\frac1n
\left(\frac{\sin(n\theta/2)}{\sin(\theta/2)}\right)^2
=:F_n(\theta),
}
\tag{25}
\]

with its continuous value at `theta=0`.  This is the classical Fejer kernel.  Hence

\[
\boxed{P_n^*m=F_n\,m.}
\tag{26}
\]

Using (12),

\[
\boxed{(P_n^*)^rm=F_{n^r}\,m\Longrightarrow\delta_0.}
\tag{27}
\]

The convergence in (27) is exactly the standard Fejer approximate-identity phenomenon from classical Fourier analysis.  This is an important falsifying control: the endpoint attraction does not encode a hidden arithmetic distinction.  It is already forced by ordinary harmonic analysis of every integer circle cover.

## 6. Transfer-operator classicalization

The Markov operator itself is a singular Doob transform of the standard inverse-branch transfer operator.  Define

\[
(L_nf)(\phi)
:=
\frac1n\sum_{T_n\theta=\phi}f(\theta).
\tag{28}
\]

On the punctured circle put

\[
h(\phi)=\frac1{\ell(\phi)}.
\tag{29}
\]

The normalization identity in (8) is equivalent to

\[
\sum_{T_n\theta=\phi}\frac1{\ell(\theta)}
=
\frac{n^2}{\ell(\phi)},
\]

so

\[
\boxed{L_nh=nh.}
\tag{30}
\]

Consequently

\[
\boxed{
P_nf
=
\frac{L_n(hf)}{nh}.
}
\tag{31}
\]

Transfer/Perron--Frobenius operators, Doob `h`-transforms, Fejer kernels, and relative-entropy chain rules are all classical.  A directed prior-art audit over those terms found the surrounding machinery rather than a new arithmetic positivity theorem.  No novelty is claimed for any of those ingredients.  The durable Mathia-specific statement is the exact identification of the `WP-104` operator-Jensen cover defect with this alias/Doob semigroup and the resulting rigidity: the only semigroup-stationary bulk state is the same singular endpoint already encountered independently in the cover-covariant positive-form classification.

## 7. This does not contradict `WP-077`

`WP-077` classifies positive **basepoint averages invariant under direct power-map pushforward** and obtains a pointed-plus-Haar family.  The present `P_n` is a different object: it is a weighted **backward alias kernel**, or equivalently the Doob transform (31).  Haar is not stationary for it; equation (26) sends Haar to a Fejer density.

Thus

\[
\boxed{
\text{direct power-map invariance}
\ne
\text{alias-Markov stationarity}.
}
\tag{32}
\]

The two findings are compatible.  In fact the comparison is useful: direct semigroup invariance leaves a Haar component, while the particular positive Jensen geometry of `WP-104` supplies a strict Lyapunov observable and removes that freedom.

## 8. Why the forced endpoint still fails the Weil mandate

The new result strengthens canonicality but does not repair any of the global obstructions.

First, `WP-094` proves that the positive exact-cover-covariant block-Toeplitz cone collapses to endpoint evaluation and that every nonzero survivor is nonclosable in the ambient `ell^2` topology.  `WP-095` similarly shows that finite-band positive energy cannot regularize the endpoint anchor.  The dynamics above therefore canonically selects precisely the state that the independent energy analysis declares singular.

Second, nothing in (10)--(31) distinguishes primes from composites.  Every integer degree `n>=2` has the same positive cocycle and the same unique attractor.  At the endpoint,

\[
\delta_0(j_n)=\log n,
\tag{33}
\]

and (16) reduces to ordinary logarithmic additivity.  Along a prime tower `p^a`, each one-step cocycle increment contributes `log p`; but reading only primitive Euler rays is still an additional arithmetic selector.  If instead one applies the canonical divisor-Mobius primitive to extract exact prime-power support, `WP-078` proves that the operator primitive is nonzero trace-zero and indefinite as soon as two distinct primes occur.

Third, the construction contains no archimedean completion, Gamma term, polar/global counterterm, or local-to-global identity with the Weil quadratic form.  The independent positivity theorem is real, but it is positivity of a universal circle-cover/Jensen process, not yet positivity of a global arithmetic pairing.

Hence the exact implication is

\[
\boxed{
\begin{array}{c}
\text{Mathia weighted Dirichlet cover geometry}\\
\Downarrow\\
\text{positive operator Jensen cocycle}\\
\Downarrow\\
\text{alias Markov semigroup with strict }\ell\text{-contraction}\\
\Downarrow\\
\delta_0\text{ uniquely forced}\\
\Downarrow\\
\text{Fejer / singular endpoint, not a regular global Weil form.}
\end{array}
}
\tag{34}
\]

## 9. What this closes and what remains open

This finding closes a specific escape left by `WP-105`: **one cannot obtain a different regular probability state by demanding coherence under the canonical positive alias-refinement semigroup.**  Coherence does not spread the exact `log n` state into the bulk; it contracts every bulk state to the endpoint.

It also strengthens the matched-control diagnosis.  The endpoint is dynamically canonical, but its canonicality is universal harmonic analysis rather than arithmetic specificity.  Therefore it cannot by itself answer the research line's primary question.

The result does **not** rule out:

1. full operator states retaining finite-section boundary/compact corrections absent from the principal-symbol algebra;
2. a non-Toeplitz, genuinely global cross-prime coupling formed before scalarization;
3. a cohomological/intersection construction with an independent global sign theorem;
4. an archimedean sector coupled nonseparably to the finite geometry before the positivity theorem;
5. a geometric quotient whose prime-power support is forced independently rather than inserted by Euler-ray restriction or signed Mobius inversion.

Any such survivor must now beat a sharper control: if its positive cover component reduces to the `WP-104` principal-symbol dynamics, semigroup coherence forces the singular Fejer endpoint rather than a new finite-energy arithmetic state.
