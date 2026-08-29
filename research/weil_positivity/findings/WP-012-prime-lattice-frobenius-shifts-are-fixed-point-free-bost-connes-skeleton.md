# WP-012 — Prime-Lattice multiplication correspondences are fixed-point-free and already form the Bost–Connes skeleton

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`.

WP-011 showed that the canonical vertical-cycle lift of a Prime-Lattice axis is null for arithmetic-surface intersection, leaving a much narrower escape: perhaps the intrinsic multiplicative semigroup of the exponent lattice itself supplies the missing analogue of Frobenius correspondences. The obvious construction is exact and canonical, but it fails in two complementary ways. On the raw Prime Lattice, nontrivial multiplication correspondences have no fixed points and zero ordinary weighted Lefschetz trace. Their positive boundary defects recover ordinary Euler factors, while the von Mangoldt weights appear only after a logarithmic derivative, i.e. after returning to the classical Euler-product/determinant mechanism. Moreover, the same semigroup isometries and logarithmic Hamiltonian are precisely the multiplicative skeleton of the Bost–Connes system; the established route that upgrades them to Frobenius-like/cohomological data is the endomotive program of Connes–Consani–Marcolli. Thus

```text
Prime-Lattice multiplication semigroup
    -> Frobenius-like correspondence
    -> independent Hodge/Weil positivity
```

does not survive as a new intrinsic route. The raw lattice has trivial fixed-point data; the nontrivial enrichment is already close Connes/endomotive prior art and still does not supply an independent theorem of Weil positivity.

## 1. The intrinsic semigroup correspondence

Write the Prime Lattice as the free commutative monoid

\[
\Lambda=\mathbb N_0^{(\mathcal P)},
\qquad
v(n)=(v_p(n))_p,
\]

with finite support and

\[
v(mn)=v(m)+v(n).
\]

For every integer `m>=1`, the most literal intrinsic correspondence is translation by its exponent vector,

\[
\tau_m(v)=v+v(m).
\tag{1}
\]

On

\[
\mathcal H=\ell^2(\Lambda)\cong\ell^2(\mathbb N^\times),
\]

let

\[
S_m\delta_v=\delta_{v+v(m)}.
\tag{2}
\]

Then

\[
S_mS_n=S_{mn},
\qquad
S_m^*S_m=I,
\tag{3}
\]

so `(S_m)` is an isometric representation of the multiplicative semigroup. In the integer basis `e_n`, equation (2) is simply

\[
S_m e_n=e_{mn}.
\tag{4}
\]

The Prime-Lattice logarithmic energy is

\[
A e_n=(\log n)e_n.
\tag{5}
\]

Hence

\[
e^{itA}S_m e^{-itA}=m^{it}S_m,
\tag{6}
\]

and, for `beta>1`,

\[
\operatorname{Tr}(e^{-\beta A})
=\sum_{n\ge1}n^{-\beta}
=\zeta(\beta).
\tag{7}
\]

Equations (4)--(7) are not a new number-theoretic dynamical system. They are exactly the multiplicative-isometry/logarithmic-Hamiltonian skeleton appearing in the canonical Bost–Connes representation. The full Bost–Connes system has additional phase/Galois algebraic data that the bare exponent lattice does not contain, so the identification here is deliberately only of this skeleton.

## 2. The raw correspondence has no Frobenius-style fixed points

For `m>1` and `r>=1`,

\[
\tau_m^r(v)=v+r\,v(m).
\]

Because `v(m)` is a nonzero vector with nonnegative integer coordinates,

\[
\tau_m^r(v)=v
\quad\Longleftrightarrow\quad
r\,v(m)=0,
\]

which is impossible. Therefore

\[
\boxed{\operatorname{Fix}(\tau_m^r)=\varnothing\qquad(m>1,r\ge1).}
\tag{8}
\]

This is already qualitatively opposite to the function-field Frobenius situation used in WP-011, where intersections of the diagonal with graphs of Frobenius iterates encode extension-field point counts.

The Hilbert-space trace says the same thing. Since `e^{-beta A}` is trace class for `beta>1` and `S_m^r` is bounded,

\[
\operatorname{Tr}(e^{-\beta A}S_m^r)
=\sum_{n\ge1}
\langle e_n,e^{-\beta A}e_{m^r n}\rangle
=0.
\tag{9}
\]

Thus the most direct ordinary Lefschetz/thermal trace of the intrinsic multiplication correspondence is identically zero for every nontrivial iterate. It cannot generate the finite Weil atoms

\[
(\log p)p^{-r/2}>0.
\tag{10}
\]

This is an exact obstruction, not a convergence artifact: the trace calculation is performed in the honest trace-class region `beta>1`.

## 3. Positive boundary defects give Euler factors, not von Mangoldt weights

Although the correspondence trace vanishes, its range defect is a canonical positive projection. For a prime `p`,

\[
D_{p,r}:=I-S_{p^r}S_{p^r}^*\ge0.
\tag{11}
\]

It projects onto basis states whose integer label is not divisible by `p^r`. Consequently, for `beta>1`,

\[
\begin{aligned}
\operatorname{Tr}(e^{-\beta A}D_{p,r})
&=\sum_{p^r\nmid n}n^{-\beta}\\
&=\zeta(\beta)-p^{-r\beta}\zeta(\beta)\\
&=\boxed{\zeta(\beta)(1-p^{-r\beta})}.
\end{aligned}
\tag{12}
\]

After normalizing by the partition function, the positive defect therefore produces

\[
1-p^{-r\beta},
\tag{13}
\]

an ordinary Euler-factor quantity. This is genuine semigroup/boundary geometry, but it still has the wrong structure for the Weil coefficient.

For `r=1`, the desired prime-power series is recovered only after applying a logarithmic derivative to the reciprocal Euler factor:

\[
-\frac{d}{d\beta}
\log(1-p^{-\beta})^{-1}
=\sum_{k\ge1}(\log p)p^{-k\beta}.
\tag{14}
\]

Equivalently,

\[
\frac{d}{d\beta}\log(1-p^{-\beta})^{-1}
=-\frac{(\log p)p^{-\beta}}{1-p^{-\beta}}.
\]

At `beta=1/2` the positive coefficients on the right of (14) become the WP-004 finite Weil weights.

Equation (14) is the decisive audit point: the semigroup's positive range defect does not itself produce the Mangoldt measure. The correct coefficients appear only after the classical `log Euler product -> logarithmic derivative` operation. Calling that operation a new boundary positivity mechanism would merely repackage the known zeta/determinant channel that this research line explicitly excludes.

Moreover, the positive trace in (12) exists only for `beta>1`. Moving it to `beta=1/2` requires analytic continuation or another nontrivial completion; ordinary trace positivity does not cross that boundary automatically.

## 4. The axis Fredholm defect has the wrong repetition weight

The same obstruction is visible without a Gibbs trace. Restrict to a single prime axis

\[
\mathcal H_p=\overline{\operatorname{span}}\{e_{p^a}:a\ge0\}.
\]

There `S_p` is the unilateral shift `U`. The basic boundary defect

\[
I-UU^*
\]

is rank one and positive, while

\[
I-U^rU^{*r}
\]

has rank `r`. Equivalently,

\[
\operatorname{ind}(U^r)=-r.
\tag{15}
\]

The energy commutator also counts repetitions:

\[
[A,U^r]=r(\log p)U^r.
\tag{16}
\]

But the von Mangoldt value on a prime power is

\[
\Lambda(p^r)=\log p,
\tag{17}
\]

not `r log p`. Thus the most canonical index/boundary and energy-cocycle data carry an unavoidable factor `r`.

WP-004 removes exactly this repetition count by the intrinsic occupation inverse `N^{-1}` on the axis:

\[
QAN^{-1}Q\,e_{p^r}=(\log p)e_{p^r}.
\]

That identity remains useful, but the present correspondence calculation shows that the shift/Fredholm geometry does not independently force the division by `r`. In determinant/dynamical-zeta language the same division comes from the standard `1/r` in

\[
-\log(1-z)=\sum_{r\ge1}\frac{z^r}{r},
\]

again returning to a classical logarithmic trace/determinant mechanism rather than an independently positive intersection form.

## 5. The other obvious lattice endomorphism is also fixed-point trivial

A second Frobenius analogy is the power map on the monoid,

\[
\rho_r(v)=rv,
\tag{18}
\]

which corresponds to `n -> n^r`. For `r>1`,

\[
rv=v
\quad\Longleftrightarrow\quad
v=0.
\tag{19}
\]

So its fixed-point set on the exponent lattice is just the vacuum, independently of the prime system. It cannot encode a hierarchy of local prime-power weights either.

This does not contradict algebraic constructions in which a power endomorphism on a richer object has many torsion fixed points. It shows precisely that those fixed points come from structure absent from the raw exponent monoid.

## 6. Prior art: the natural enrichment is already the Bost–Connes/endomotive route

Bost and Connes constructed a quantum statistical system for `Q` whose canonical representation contains the integer multiplication isometries and the Hamiltonian `log n`, with partition function `zeta(beta)`. The exact Prime-Lattice operators (4)--(7) therefore sit inside established operator-algebraic prior art rather than defining a new Frobenius correspondence theory.

Connes, Consani, and Marcolli subsequently formalized the relevant enlargement through **endomotives**. Their construction starts from semigroups of algebraic endomorphisms; the semigroup of endomorphisms of the multiplicative group yields the Bost–Connes system. In that framework the characteristic-zero analogue of Frobenius is not the raw shift (1): it is the scaling action on cyclic homology of a cokernel in a larger noncommutative/cohomological category, giving a spectral realization of zeta/L-function zeros and an archimedean Lefschetz formula.

Their later `Fun with F1` makes the novelty boundary even closer to the present proposal: the Bost–Connes endomotive is described over an `F1`-type arithmetic geometry in which its endomorphisms explicitly reflect Frobenius correspondences.

Therefore an attempted repair of (8)--(19) by adjoining torsion/phase data, a cokernel, cyclic homology, a scaling action, or an adelic trace object immediately enters a well-developed Connes/endomotive prior-art family. Such an enlargement may remain mathematically relevant, but it cannot be reported as a Mathia-native positivity mechanism unless Mathia forces additional structure and, crucially, proves a sign theorem not already equivalent to the desired Weil positivity.

## 7. Matched-control obstruction

The exact semigroup argument is not special to the ordinary primes. Let a free commutative monoid have generators `q` with arbitrary positive lengths `ell(q)`, and set

\[
A\,e_x=E(x)e_x,
\qquad
E(xy)=E(x)+E(y).
\]

The left translations remain isometries, nontrivial translations remain fixed-point-free, axis restrictions remain unilateral shifts, and whenever the corresponding partition series converges the normalized range-defect trace is the generalized Euler factor

\[
1-e^{-\beta r\ell(q)}.
\]

Thus the raw correspondence, boundary positivity, repetition index, and logarithmic-derivative repair survive generalized-prime replacements. They do not distinguish the rational primes from the Beurling controls that already killed the sufficiency of WP-004.

A successful global mechanism therefore cannot be merely the free multiplicative semigroup plus a positive representation of its shifts.

## 8. Consequence for the research line

WP-011 narrowed a viable intersection route to a global correspondence rather than vertical fibers. WP-012 now rules out the **most intrinsic correspondence already present in Prime Lattice** as the missing analogue:

```text
multiplication translation on exponent vectors
    -> no fixed points
    -> zero ordinary Lefschetz/thermal trace

positive range defect
    -> Euler factor
    -> Mangoldt weights only after log derivative
    -> classical zeta/determinant route

axis Fredholm defect
    -> repetition number r
    -> wrong coefficient for Lambda(p^r)

add torsion/cokernel/cohomology/Frobenius enrichment
    -> Bost–Connes / endomotive prior art.
```

This does **not** rule out every possible Mathia correspondence. It sets a sharper requirement. A surviving candidate must produce nontrivial prime-power fixed/intersection data without simply taking the left-regular multiplication shift, must force the exponent normalization that converts `r log p` to `log p`, must supply the archimedean/polar sector from the same object, and must possess an independent geometric sign theorem. If those ingredients are introduced through the known endomotive/adelic trace machinery, the novelty burden is to identify a genuinely new positivity theorem rather than another spectral or Lefschetz realization.

## 9. Falsification checklist

The core obstruction can be checked independently of RH and zeta zeros:

1. verify `S_m e_n=e_{mn}` and `e^{itA}S_m e^{-itA}=m^{it}S_m`;
2. verify that `tau_m^r` has no fixed exponent vector for `m>1`;
3. verify `Tr(e^{-beta A}S_m^r)=0` for `beta>1`;
4. verify the exact positive-defect trace `Tr(e^{-beta A}(I-S_{p^r}S_{p^r}^*))=zeta(beta)(1-p^{-r beta})`;
5. verify that the local von Mangoldt series appears only after a logarithmic derivative of the Euler factor;
6. verify on one axis that `rank(I-U^rU^{*r})=r`, `ind(U^r)=-r`, and `[A,U^r]=r log(p) U^r`;
7. compare the operator skeleton with the canonical Bost–Connes representation and the Frobenius/cyclic-homology enrichment with endomotive prior art.

A counterexample to WP-012 would need to exhibit a **different canonical correspondence forced by existing Mathia data** whose nontrivial fixed/intersection terms occur at every `p^r`, carry the exact `log p p^{-r/2}` normalization without an inserted Euler logarithmic derivative, include the archimedean completion, and satisfy an independent positivity theorem. That would be a genuinely new route rather than a normalization of the multiplication semigroup considered here.
