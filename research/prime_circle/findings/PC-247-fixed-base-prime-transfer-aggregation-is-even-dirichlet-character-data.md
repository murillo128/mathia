# PC-247 — fixed-base prime-transfer aggregation is exactly even Dirichlet-character data

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for the most direct all-scale aggregation left by PC-246 at a fixed lower prime. Once the elementary `pq I` part of the prime-prime transfer Gram matrix is removed, retaining **all** upper-prime packets at one fixed base prime and summing them linearly, averaging them over primes, or taking their Dirichlet transform does not create a new Prime-Circle analytic carrier. The whole matrix-valued family has an exact multiplicative-character decomposition. Its residue-average is a constant-weight path Laplacian, and its nonprincipal channels are classical even Dirichlet characters with geometric coefficients proportional to `L(-1,chi)`. The prime-only Dirichlet transform is therefore a finite matrix combination of Dirichlet prime `L`/prime-zeta functions, hence by Euler-product Möbius inversion of ordinary Dirichlet `L`-functions.

This is deliberately a **fixed-base linear** boundary. It does not classify simultaneous growth of the lower prime, nonlinear products coupling different lower primes, genuinely multi-prime packet networks before contraction, native composite masks, or the other nonlinear/off-circle/global-uniformization directions in the Prime-Circle mandate.

## 1. The PC-246 defect as a residue-indexed path Laplacian

Fix an odd prime `p`. For every prime `q>p`, PC-246 gives

\[
K_{p,q}^*K_{p,q}=pq\,I_p-L_{p,h},
\qquad h\equiv q\pmod p,
\tag{1}
\]

where `L_{p,h}` is the weighted path Laplacian on vertices `0,...,p-1` with edge weights

\[
w_k(h)=f_p(hk\bmod p),
\qquad
f_p(a)=a(p-a),
\qquad 1\le k<p.
\tag{2}
\]

Residues in (2) are represented by `1,...,p-1`. Thus the only nontrivial fixed-`p` matrix left after removing `pq I_p` is the function

\[
h\in G_p:=(\mathbb Z/p\mathbb Z)^\times
\longmapsto L_{p,h}.
\tag{3}
\]

Let `\mathscr L_p(v_1,...,v_{p-1})` denote the path-Laplacian map, linear in its edge sequence, so that

\[
L_{p,h}=\mathscr L_p\bigl(f_p(h),f_p(2h),\ldots,f_p((p-1)h)\bigr).
\tag{4}
\]

The question is whether keeping the entire matrix in (3), rather than one spectral statistic, and then aggregating over all upper primes can recover analytic information not already present in classical residue-class prime distributions.

## 2. Exact multiplicative Fourier decomposition of the whole matrix family

For a Dirichlet character `chi mod p`, define the multiplicative Fourier coefficient

\[
\widehat f_p(\chi)
:=\frac1{p-1}\sum_{a=1}^{p-1}a(p-a)\,\overline{\chi(a)}
\tag{5}
\]

and the fixed character path matrix

\[
B_{p,\chi}
:=\mathscr L_p\bigl(\chi(1),\chi(2),\ldots,\chi(p-1)\bigr).
\tag{6}
\]

Fourier inversion on the finite multiplicative group `G_p` gives

\[
f_p(x)=\sum_{\chi\bmod p}\widehat f_p(\chi)\chi(x).
\tag{7}
\]

Substituting `x=hk` in every edge of (4) and using linearity of `\mathscr L_p` yields the exact **matrix identity**

\[
\boxed{
L_{p,h}
=\sum_{\chi\bmod p}
\widehat f_p(\chi)\,\chi(h)\,B_{p,\chi}.
}
\tag{8}
\]

No trace, determinant, eigenvalue ordering, or asymptotic limit has been taken. Equation (8) decomposes the complete centered prime-prime packet Gram matrix entry by entry.

The symmetry `f_p(p-a)=f_p(a)` immediately kills every odd character:

\[
\boxed{
\widehat f_p(\chi)=0
\qquad\text{if }\chi(-1)=-1.
}
\tag{9}
\]

For the principal character `chi_0`, the elementary power sum gives

\[
\boxed{
\widehat f_p(\chi_0)
=\frac1{p-1}\sum_{a=1}^{p-1}a(p-a)
=\frac{p(p+1)}6.
}
\tag{10}
\]

For a nonprincipal even character, pairing `a` with `p-a` shows `sum_a a chi(a)=0`. The generalized Bernoulli special-value identity already anchored in `SOURCES.md` gives

\[
\sum_{a=1}^{p-1}a^2\overline{\chi(a)}
=-2p\,L(-1,\overline\chi),
\tag{11}
\]

and hence

\[
\boxed{
\widehat f_p(\chi)
=\frac{2p}{p-1}L(-1,\overline\chi),
\qquad
\chi\ne\chi_0,\quad \chi(-1)=1.
}
\tag{12}
\]

Thus the geometry separates exactly into fixed finite path matrices `B_{p,chi}` and classical special values `L(-1,chi)`. The parity loss is also intrinsic: PC-246 already proved `L_{p,h}=L_{p,-h}`, and (9) is precisely that quotient in multiplicative Fourier coordinates.

## 3. Prime averaging converges to a universal constant-weight path

Averaging (8) over all nonzero residues kills every nonprincipal character, so

\[
\boxed{
\overline L_p
:=\frac1{p-1}\sum_{h=1}^{p-1}L_{p,h}
=\frac{p(p+1)}6\,\Delta_p,
}
\tag{13}
\]

where `Delta_p=B_{p,chi_0}` is the ordinary unit-edge path Laplacian on `p` vertices.

Its spectrum is therefore explicit:

\[
\boxed{
\operatorname{Spec}(\overline L_p)
=
\left\{
\frac{p(p+1)}3
\left(1-\cos\frac{j\pi}{p}\right)
:0\le j<p
\right\}.
}
\tag{14}
\]

For fixed `p`, the prime number theorem in arithmetic progressions makes the residue classes of primes `q` asymptotically equidistributed in `G_p`. Consequently

\[
\boxed{
\frac{1}{\#\{q\le X:q>p,\ q\text{ prime}\}}
\sum_{\substack{p<q\le X\\q\text{ prime}}}L_{p,q\bmod p}
\longrightarrow
\overline L_p.
}
\tag{15}
\]

The leading all-upper-prime average therefore forgets primality completely after equidistribution: it is just the constant-weight finite-difference path operator (13). All arithmetic fluctuation around that limit lies in the nonprincipal even character channels of (8), i.e. in the standard prime-number-in-arithmetic-progressions data modulo `p`.

A small exact control makes the content transparent. For `p=5`,

\[
f_5=(4,6,6,4),
\qquad
\widehat f_5(\chi_0)=5,
\tag{16}
\]

and the only nonprincipal even character is the quadratic character `chi_2`, for which `widehat f_5(chi_2)=-1`. Hence

\[
\boxed{L_{5,h}=5\Delta_5-\chi_2(h)B_{5,\chi_2}.}
\tag{17}
\]

The complete matrix variation over every upper prime `q>5` is therefore exactly one quadratic residue-class prime race, not a new transfer-spectrum variable. For `p=3` there is no nonprincipal even channel at all, in agreement with the fact that the signed-residue quotient has only one element.

## 4. The prime-only Dirichlet transform is a finite packet of classical Dirichlet prime L-functions

The most direct analytic all-scale aggregation of the PC-246 defects is their prime-only Dirichlet transform. For `Re(s)>1`, put

\[
\mathcal F_p(s)
:=
\sum_{\substack{q>p\\q\text{ prime}}}
\frac{L_{p,q\bmod p}-\overline L_p}{q^s}.
\tag{18}
\]

Using (8)--(13),

\[
\boxed{
\mathcal F_p(s)
=
\sum_{\substack{\chi\bmod p\\
\chi\ne\chi_0,\ \chi(-1)=1}}
\widehat f_p(\chi)\,B_{p,\chi}\,
P_{\chi,>p}(s),
}
\tag{19}
\]

where

\[
P_{\chi,>p}(s)
:=\sum_{\substack{q>p\\q\text{ prime}}}\frac{\chi(q)}{q^s}.
\tag{20}
\]

The omitted primes below `p` form only a finite Dirichlet polynomial. If

\[
P_\chi(s):=\sum_{q\text{ prime}}\frac{\chi(q)}{q^s},
\tag{21}
\]

then the Euler product for the ordinary Dirichlet `L`-function gives

\[
\log L(s,\chi)
=\sum_{m\ge1}\frac1m P_{\chi^m}(ms).
\tag{22}
\]

Möbius inversion in the exponent therefore gives the exact identity

\[
\boxed{
P_\chi(s)
=\sum_{m\ge1}\frac{\mu(m)}m
\log L(ms,\chi^m),
\qquad \Re(s)>1.
}
\tag{23}
\]

Indeed, substituting (22) into the right side makes the coefficient of `P_{chi^r}(rs)` equal to

\[
\frac1r\sum_{m\mid r}\mu(m),
\tag{24}
\]

which is `1` for `r=1` and `0` otherwise. Thus (19) is not merely analogous to Dirichlet-character prime statistics: it is **exactly a finite matrix-valued linear combination of them**, and (23) places each channel inside the classical Dirichlet-`L` Euler-product package.

If the residue mean is not removed, one simply adds the principal channel

\[
\frac{p(p+1)}6\,\Delta_p\,P_{\chi_0,>p}(s),
\tag{25}
\]

with

\[
L(s,\chi_0)=\zeta(s)(1-p^{-s}).
\tag{26}
\]

Hence the Riemann zeta function enters this fixed-base transform only through the standard principal Dirichlet-character Euler product. After mean subtraction the remaining channels are nonprincipal even Dirichlet `L`-functions. Continuing (23) wherever a branch is chosen can only inherit logarithmic singularities from poles and zeros of the classical factors `L(ms,chi^m)` (together with their scaled copies); it does not produce a new independently derived zero divisor or a distinguished functional equation of its own.

## 5. What information survives: exactly the even residue-class prime fluctuations

Equation (8) makes the information boundary sharper than a scalar averaging argument. At fixed `p`, **every matrix entry and every fixed linear functional of the full PC-246 defect family is a finite even-character Fourier series in `q mod p`**. Summing such data over upper primes therefore produces finite linear combinations of the usual character-weighted prime sums.

Conversely, the geometric coefficients in the nonprincipal even channels are the classical values (12), and the path matrices in (6) retain the same finite character labels. Thus any unexpectedly small or square-root-scale cancellation in the all-upper-prime aggregate is a statement in the established even-character prime-number-race / prime-number-theorem-in-arithmetic-progressions problem. Standard explicit formulas relate those fluctuations to zeros of the corresponding Dirichlet `L(s,chi)`. Calling the resulting criterion a new Prime-Circle route to the Riemann hypothesis would merely relabel that classical analytic-number-theory content.

This also supplies a matched nonarithmetic control stronger than one numerical prime/composite comparison. The reduction from a finite residue-dependent matrix function `h -> A_h` to character channels is generic finite-group Fourier analysis. The specific Prime-Circle input here is the elementary weight `f_p(a)=a(p-a)` forced by PC-246; its Fourier coefficients happen to be the classical `L(-1,chi)` values in (12). The all-scale analytic step itself is not generated by new two-dimensional roots-of-unity geometry.

## 6. Prior-art and novelty audit

No novelty is claimed for finite multiplicative Fourier analysis, Dirichlet characters, generalized Bernoulli special values, the prime number theorem in arithmetic progressions, Euler products, Möbius inversion, Dirichlet prime `L`-functions, or prime-zeta-type transforms. `research/prime_circle/SOURCES.md` already anchors the generalized-Bernoulli identity used in (11)--(12), multiplicative character methods, and the standard Dirichlet-series/Euler-product boundary relevant to earlier Prime-Circle collapses.

A targeted literature check confirms that prime-restricted Dirichlet-character series are an established object (often called Dirichlet Prime `L`-functions or prime-zeta-modulo functions), and standard references on Dirichlet `L`-functions place arithmetic-progression prime fluctuations and their explicit formulas directly in the zero theory of those `L`-functions. The negative conclusion does not rely on an absence-of-literature claim: equations (8), (13), and (19)--(23) give the complete reduction algebraically.

The project-local result is the boundary theorem linking that classical package to the exact packet geometry of PC-246. Keeping the full matrix, all upper-prime labels, and an analytic scale variable still does not evade classicalization when the lower prime is fixed and the aggregation is linear.

## 7. Research consequence and remaining boundary

The chain

\[
\boxed{
\text{fixed lower prime }p
\longrightarrow
\{K_{p,q}^*K_{p,q}-pqI\}_{q>p\text{ prime}}
\longrightarrow
\text{linear prime averaging / Dirichlet transform}
\longrightarrow
\text{new RH carrier}
}
\tag{27}
\]

is closed. The residue mean is the universal path Laplacian (13), while every fluctuation channel is a classical even Dirichlet character and every prime-only Dirichlet channel is given by (23).

This does **not** close the simultaneous-growth frontier identified by PC-245/PC-246. A surviving packet mechanism must couple changing lower conductors before fixed-base Fourier reduction becomes applicable, retain nonlinear relations among several packet bases, derive a source-forced topology or normalization in a joint `p,q,... -> infinity` limit, or leave the affine/polyphase transfer category through a genuinely nonlinear/off-circle/global geometric construction. In particular, a three-or-more-conductor network whose invariant cannot be written as a sum of separate fixed-base residue functions remains outside this result.

## Falsification checks

The finding can be audited without numerical inference. Starting from PC-246, verify (8) directly by finite-group Fourier inversion and path-Laplacian linearity; pair `a` with `p-a` to check (9); evaluate the principal power sum for (10); use the standard generalized-Bernoulli identity to check (11)--(12); average (8) to obtain (13) and diagonalize the ordinary path Laplacian for (14); check the `p=5` decomposition (17) entry by entry; and substitute the Euler-product expansion (22) into (23), where ordinary Möbius cancellation leaves only the first prime-power exponent. A failure of any of these exact identities changes the conclusion. Otherwise the fixed-base linear all-upper-prime aggregation is completely reduced to classical even Dirichlet-character data.