# WP-152 — Natural shell-size cutoff leaves only a universal root boundary layer

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIME-CIRCLE + CYCLOTOMIC-RESULTANT + NORMALIZED-LAPLACIAN + NATURAL-SHELL-CUTOFF + BOUNDARY-MASS + STRONG-WEAK-LIMIT-SEPARATION + PRIME-NUMBER-THEOREM + MATCHED-REGULAR-VARIATION-CONTROL + PRIOR-ART-AUDITED`

## Claim

`WP-151` showed that normalized-adjacency mass escaping every fixed finite core is not an intrinsic datum of the all-prime resultant graph under an unspecified exhaustion: star-dominant and cube-dominant exhaustions give incompatible strong behavior already at the root. It deliberately left open a narrower possibility: Prime Circle has an intrinsic shell index, so perhaps the arithmetic-size exhaustion

\[
F_X=\{1,2,\ldots,X\}
\tag{1}
\]

selects a distinguished moving positive response.

That natural cutoff can be evaluated exactly enough to close the proposed escape. Let

\[
J_{m,n}
=
\frac{\log|\operatorname{Res}(\Phi_m,\Phi_n)|}
{\sqrt{\varphi(m)\varphi(n)}}\ge0,
\qquad
N_X=D_X^{-1/2}J_XD_X^{-1/2},
\tag{2}
\]

where `J_X` is restricted to `F_X` and `D_X` is its finite weighted degree matrix. Then:

1. for every fixed non-root shell `m\ge2`,
   \[
   \boxed{\|N_X\delta_m\|\longrightarrow0;}
   \tag{3}
   \]
2. at the root,
   \[
   \boxed{
   N_X\delta_1\rightharpoonup0,
   \qquad
   \|N_X\delta_1\|^2
   \longrightarrow
   1-\frac1{\sqrt2};
   }
   \tag{4}
   \]
3. after rescaling the moving shell coordinate by `n/X`, the entire surviving squared mass converges to
   \[
   \boxed{
   d\nu(u)
   =
   \mathbf 1_{(1/2,1]}(u)\,
   \frac{du}{2\sqrt u}.
   }
   \tag{5}
   \]

The residual state therefore has a very concrete origin: it consists asymptotically only of **prime leaves in the top half of the cutoff**, `X/2<p\le X`. All fixed prime-power coefficients disappear, every non-root fixed shell has strong normalized-adjacency collapse, and the rescaled root profile depends only on the first-order regular variation supplied by the prime number theorem.

Thus the most obvious shell-size choice left open by `WP-151` does pick a deterministic escaped boundary layer, but that layer is not a Weil finite-prime selector and does not produce an archimedean/global counterterm. Its limiting law is reproduced by a generic weighted rooted graph with the same `X^{1/2}` cumulative edge growth and the same cutoff-leaf geometry. The finite normalized Laplacians remain positive for the independent graph-Dirichlet reason, but their only non-strong fixed-shell defect is a universal cutoff boundary effect at the trivial shell `1`.

This does not rule out a different Mathia-forced topology, a nonlocal completion, a source-derived moving test space carrying more than shell size, or a finite--archimedean coupling formed before normalization. It rules out interpreting the natural `1,\ldots,X` normalized root escape itself as the missing global Weil-positive arithmetic datum.

## 1. Exact root weights and their cumulative asymptotic

`WP-148` gives, for a fresh prime step,

\[
J_{m,mp}
=
a_p,
\qquad
a_p:=\frac{\log p}{\sqrt{p-1}}.
\tag{6}
\]

At the root, all neighbors are prime powers. More precisely,

\[
J_{1,p^k}
=
b_{p,k}
:=
\frac{\log p}
{p^{(k-1)/2}\sqrt{p-1}},
\qquad k\ge1.
\tag{7}
\]

Write

\[
A(X):=\sum_{p\le X}a_p.
\tag{8}
\]

Since

\[
a_p
=
\frac{\log p}{\sqrt p}
\left(1+O\!\left(\frac1p\right)\right),
\tag{9}
\]

the prime number theorem and partial summation give

\[
\boxed{
A(X)=2\sqrt X+o(\sqrt X).
}
\tag{10}
\]

The higher prime-power part of the root degree is lower order. Indeed,

\[
H(X)
:=
\sum_{\substack{k\ge2\\p^k\le X}}b_{p,k}
\ll
\sum_{p\le\sqrt X}
\frac{\log p}{p}
\sum_{j\ge0}p^{-j/2}
=
O(\log X).
\tag{11}
\]

Consequently

\[
d_X(1)
=
A(X)+H(X)
=
\boxed{2\sqrt X+o(\sqrt X)}.
\tag{12}
\]

Only this first-order prime asymptotic will survive in the moving root state.

## 2. The top-half primes are exact leaves

If

\[
\frac X2<p\le X
\tag{13}
\]

is prime, then `p` has no upward prime-power-ratio neighbor inside `F_X`: every proper multiple of `p` is larger than `X`. Since `p` itself is prime, its only downward resultant neighbor is `1`. Hence `p` is an exact weighted leaf and

\[
d_X(p)=a_p.
\tag{14}
\]

Its squared normalized-adjacency coefficient at the root is therefore

\[
\left|
\langle\delta_p,N_X\delta_1\rangle
\right|^2
=
\frac{a_p^2}{d_X(1)a_p}
=
\frac{a_p}{d_X(1)}.
\tag{15}
\]

The total contribution of these leaf primes is

\[
R_X^{\mathrm{leaf}}
=
\frac{A(X)-A(X/2)}{d_X(1)}.
\tag{16}
\]

Equations (10) and (12) immediately give

\[
\boxed{
R_X^{\mathrm{leaf}}
\longrightarrow
1-\frac1{\sqrt2}.
}
\tag{17}
\]

So the nonzero limiting root norm is not hidden in fixed arithmetic coordinates. It is already forced by the most elementary boundary layer of the induced shell cutoff.

## 3. Every other root-neighbor contribution vanishes

It remains to show that (17) is the **whole** limiting norm.

First consider prime neighbors `p\le X/2`. Apart from the single prime `p=2`, every such prime is odd, so `2p\le X` and the fresh direction `2` supplies the second edge

\[
J_{p,2p}=a_2=\log2.
\tag{18}
\]

Thus

\[
d_X(p)\ge a_2
\qquad
(2<p\le X/2).
\tag{19}
\]

The total contribution of these nonleaf prime neighbors is bounded by

\[
\frac1{d_X(1)}
\sum_{p\le X/2}
\frac{a_p^2}{d_X(p)}
\ll
\frac1{\sqrt X}
\sum_{p\le X}
\frac{(\log p)^2}{p-1}.
\tag{20}
\]

Even the crude comparison with all integers gives

\[
\sum_{p\le X}
\frac{(\log p)^2}{p-1}
=
O((\log X)^3),
\tag{21}
\]

so (20) tends to zero.

Now consider root neighbors `p^k` with `k\ge2`. Since the root edge itself is part of the degree,

\[
d_X(p^k)\ge b_{p,k},
\tag{22}
\]

and hence their total squared-norm contribution is at most

\[
\frac1{d_X(1)}
\sum_{\substack{k\ge2\\p^k\le X}}
b_{p,k}
=
O\!\left(\frac{\log X}{\sqrt X}\right)
\longrightarrow0
\tag{23}
\]

by (11).

Combining (17), (20), and (23),

\[
\boxed{
\|N_X\delta_1\|^2
\longrightarrow
1-\frac1{\sqrt2}.
}
\tag{24}
\]

For every fixed shell `n\ne1`, `WP-150` already gives

\[
\langle\delta_n,N_X\delta_1\rangle
=
\frac{J_{1,n}}
{\sqrt{d_X(1)d_X(n)}}
\longrightarrow0.
\tag{25}
\]

Since `\|N_X\|\le1`, finite-support vectors are dense and therefore

\[
N_X\delta_1\rightharpoonup0.
\tag{26}
\]

Equations (24) and (26) prove the root statement (4): the natural size exhaustion still has no strong root limit.

## 4. The escaped root state has a universal boundary profile

The moving mass can be described more sharply. Put a finite positive measure on the rescaled shell coordinate by

\[
\nu_X
:=
\sum_{\substack{n\le X\\n\ne1}}
\left|
\langle\delta_n,N_X\delta_1\rangle
\right|^2
\delta_{n/X}.
\tag{27}
\]

Sections 2--3 show that all mass outside the top-half prime leaves is `o(1)`. For any fixed

\[
\frac12<a<b\le1,
\tag{28}
\]

equation (15) therefore gives

\[
\nu_X((a,b])
=
\frac{A(bX)-A(aX)}{d_X(1)}
+o(1).
\tag{29}
\]

Using (10)--(12),

\[
\boxed{
\nu_X((a,b])
\longrightarrow
\sqrt b-\sqrt a.
}
\tag{30}
\]

These interval limits identify the weak limit

\[
\boxed{
\nu_X
\Rightarrow
\nu,
\qquad
d\nu(u)
=
\mathbf1_{(1/2,1]}(u)
\frac{du}{2\sqrt u}.
}
\tag{31}
\]

Its total mass is exactly

\[
\nu((1/2,1])
=
1-\frac1{\sqrt2},
\tag{32}
\]

matching (24).

This is useful because it removes a possible ambiguity in the phrase "mass escapes to infinity." Under the most natural shell scaling, the escape is not an unresolved arithmetic cloud. It has an explicit continuum law, supported entirely on the artificial outer boundary where newly admitted primes have not yet acquired even their first multiplicative child.

## 5. Every fixed non-root shell collapses strongly

The root is exceptional. Fix `m\ge2`. Fresh-prime children alone give

\[
d_X(m)
\ge
\sum_{\substack{p\le X/m\\p\nmid m}}a_p
=
2\sqrt{X/m}+o(\sqrt X),
\tag{33}
\]

so in particular

\[
d_X(m)\gg_m\sqrt X.
\tag{34}
\]

We estimate

\[
\|N_X\delta_m\|^2
=
\frac1{d_X(m)}
\sum_{\substack{n\le X\\n\ne m}}
\frac{J_{m,n}^2}{d_X(n)}.
\tag{35}
\]

There are only finitely many downward prime-power-ratio neighbors of `m`, and their contribution to the sum in (35) is bounded independently of `X`.

There are also only finitely many prime directions `p\mid m`. Along each such outward ray, `WP-148` gives geometrically decaying weights `(\log p)p^{-k/2}`, so those directions contribute only `O_m(1)` before division by `d_X(m)`.

The potentially dangerous family is the first fresh-prime layer `n=mp`, `p\nmid m`, because its edge weight is again `a_p`. Choose once and for all a prime-power factor

\[
q^e\Vert m,
\qquad
m_0:=m/q^e.
\tag{36}
\]

For every fresh prime `p\nmid m`, the child `mp` has the additional neighbor `m_0p`, and

\[
\frac{mp}{m_0p}=q^e.
\tag{37}
\]

Because `q\nmid m_0p`, the fresh-prime-power formula from `WP-148` gives the fixed positive edge

\[
J_{m_0p,mp}
=
c_m
:=
\frac{\log q}
{q^{(e-1)/2}\sqrt{q-1}}
>0,
\tag{38}
\]

independent of `p` and `X`. Both vertices lie in `F_X` whenever `mp\le X`. Hence

\[
d_X(mp)\ge c_m.
\tag{39}
\]

The entire first fresh layer therefore contributes at most

\[
\sum_{\substack{p\le X/m\\p\nmid m}}
\frac{a_p^2}{d_X(mp)}
\le
\frac1{c_m}
\sum_{p\le X/m}a_p^2
=
O_m((\log X)^3).
\tag{40}
\]

For fresh powers `mp^k` with `k\ge2`, use `d_X(mp^k)\ge J_{m,mp^k}` exactly as at the root. The sum of the resulting upper bounds is `O(\log X)`. Combining all neighbor classes with (34),

\[
\boxed{
\|N_X\delta_m\|^2
=
O_m\!\left(\frac{(\log X)^3}{\sqrt X}\right)
\longrightarrow0
\qquad(m\ge2).
}
\tag{41}
\]

Thus under the natural cutoff the normalized Laplacian

\[
\mathcal L_X=I-N_X\succeq0
\tag{42}
\]

converges strongly to the identity on every fixed non-root basis state:

\[
\mathcal L_X\delta_m\to\delta_m
\qquad(m\ge2).
\tag{43}
\]

At the root it converges only weakly:

\[
\mathcal L_X\delta_1\rightharpoonup\delta_1,
\qquad
\|\mathcal L_X\delta_1-\delta_1\|^2
\to
1-\frac1{\sqrt2}.
\tag{44}
\]

For any fixed finitely supported vector `f` with `f_1=0`, (41) and finite dimensionality of its support imply `\mathcal L_Xf\to f` strongly. The only fixed-shell obstruction left by this cutoff is therefore the moving leaf layer attached to the trivial shell.

## 6. Matched regular-variation control

The constant and density above are not fine arithmetic invariants. The proof uses only a generic boundary mechanism.

Suppose a rooted **one-layer control graph** has root-neighbor sizes `s_j`, root weights `w_j>0`, and cumulative weight

\[
W(X):=\sum_{s_j\le X}w_j
\sim C X^\beta
\qquad(C>0,\ \beta>0).
\tag{45}
\]

Assume that neighbors with `s_j\le X/2` acquire a second edge whose weight is bounded below uniformly, while neighbors in `(X/2,X]` remain leaves, and that

\[
\sum_{s_j\le X}w_j^2=o(W(X)).
\tag{46}
\]

Then exactly the same normalized-root calculation gives

\[
\|N_X\delta_{\rm root}\|^2
\longrightarrow
1-2^{-\beta},
\tag{47}
\]

and the rescaled squared leaf mass has density

\[
\mathbf1_{(1/2,1]}(u)\,
\beta u^{\beta-1}\,du.
\tag{48}
\]

The resultant graph is the case `\beta=1/2`, with (46) following from the elementary square-weight bound used in (20). Its value `1-1/\sqrt2` and density `du/(2\sqrt u)` therefore reflect **regular variation plus induced-cutoff leaf geometry**, not the detailed prime-power selector, a Gamma factor, or a zero statistic.

This is a matched control in the sense relevant to the research mandate. The arithmetic graph forces the particular inputs, but the proposed positive escaped observable is insensitive to everything beyond their coarse cumulative growth law.

## 7. Prior art and novelty audit

The arithmetic support and exact edge values come from T. M. Apostol, *Resultants of cyclotomic polynomials*, Proceedings of the American Mathematical Society **24** (1970), 457--462, DOI `10.1090/S0002-9939-1970-0251010-X`. The asymptotic (10) is an immediate classical consequence of the prime number theorem by partial summation.

Symmetric normalized graph Laplacians are standard; see Fan R. K. Chung, *Spectral Graph Theory*, CBMS Regional Conference Series in Mathematics 92, American Mathematical Society, 1997. Relations between normalized Laplacians and induced subgraphs are also classical; for example Steve Butler, *Interlacing for weighted graphs using the normalized Laplacian*, Electronic Journal of Linear Algebra **16** (2007), DOI `10.13001/1081-3810.1185`. Infinite weighted graph exhaustion and Dirichlet-form questions are part of the standard graph-Laplacian literature already audited in `WP-148`--`WP-151`.

A bounded search for normalized-adjacency strong convergence under induced finite exhaustions, boundary mass escape for degree-normalized graphs, and cyclotomic-resultant graph Laplacians found those general frameworks but no treatment of the exact shell-size asymptotics (24), (31), or the non-root collapse (41) for this arithmetic graph. No broad graph-theory or analytic-number-theory novelty is claimed. The narrow Mathia-specific contribution is the exact consequence of combining the already-derived resultant weights with the intrinsic arithmetic-size cutoff.

This is also not a new RH-equivalent positivity criterion. No zero data or classical Weil-positive kernel enters the proof. The result is a falsification of one proposed way of extracting a global positive object from Mathia's independently positive finite resultant Laplacians.

## 8. Consequence for the Weil-positivity mandate

`WP-151` required any residual normalized-mass route to provide a source-forced exhaustion and then survive a regularization/control audit. The cutoff `F_X=\{1,\ldots,X\}` is the strongest obvious response because it uses the shell index already present in Prime Circle instead of an externally chosen star/cube ordering.

It does not recover the missing structure.

All fixed non-root shell responses collapse strongly. At the root, the surviving norm comes only from primes so close to the cutoff that their first multiplicative child is absent. After the only natural rescaling `n\mapsto n/X`, that response converges to the regular-variation law (31). It contains no local-to-global decomposition matching the finite Mangoldt term and the archimedean Gamma/polar terms, and its positivity is merely squared boundary mass inherited from the finite normalized graph.

Accordingly, the implication

\[
\boxed{
\text{Prime-Circle shell order}
+
\text{normalized resultant positivity}
+
\text{natural size exhaustion}
\;\not\Longrightarrow\;
\text{global Weil-positive geometry}.
}
\tag{49}
\]

The remaining viable space is narrower. A successful construction must add structure **before** this normalization destroys the fixed arithmetic interactions: a genuinely nonlocal/mixed-prime completion, a source-forced test-space topology carrying more than the cutoff boundary profile, or a finite--archimedean coupling whose own geometry fixes both the global completion and the sign theorem.

## 9. Falsification surface

The result would need revision if any of the following fails:

- the fresh-prime and root prime-power weights (6)--(7) are not the normalized cyclotomic-resultant values;
- the weighted prime sum in (10) does not have the stated prime-number-theorem asymptotic;
- a prime `X/2<p\le X` has a second resultant neighbor inside `F_X`;
- the secondary edge (38) fails for a fixed non-root shell and fresh prime child;
- the nonleaf or higher-prime-power contributions in (20), (23), or (40) remain of order `\sqrt X`;
- a Mathia-forced observable can use the boundary measure (31) to recover the exact Weil finite and archimedean terms while retaining an independent geometric positivity theorem, rather than inserting those terms afterwards.

The first five are explicit finite/arithmetic statements and can be checked independently. The last is intentionally left as the surviving research burden rather than assumed away.
