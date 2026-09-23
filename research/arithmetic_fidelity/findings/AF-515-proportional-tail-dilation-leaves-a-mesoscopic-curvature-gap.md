# AF-515 — Proportional tail dilation leaves a mesoscopic curvature gap

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `QUANTITATIVE-SEPARATION` · `DIRICHLET-SOURCE` · `PROPORTIONAL-TAIL-DILATION` · `MESOSCOPIC-BOUNDARY-SCALE` · `THRESHOLD-WITNESS` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
P(s)=\sum_{p\in\mathbb P}p^{-s},
\qquad
\kappa_P(s)=\frac{d^2}{ds^2}\log P(s),
\qquad s>1.
\]

Fix an integer `c\ge2`. For a cutoff `A\ge3`, retain every prime at or below `A` and dilate every prime above `A` by the common factor `c`:

\[
R_{A,c}
=
\{p\in\mathbb P:p\le A\}
\cup
\{cp:p\in\mathbb P,\ p>A\}.
\tag{1}
\]

The moved atoms are pairwise distinct composite integers. Write

\[
\kappa_{A,c}(s)
=
\frac{d^2}{ds^2}
\log\!\left(\sum_{q\in R_{A,c}}q^{-s}\right).
\]

For every fixed `k>1`, set

\[
s_A=1+t_A,
\qquad
t_A=(\log A)^{-k}.
\tag{2}
\]

Then the signed relative curvature defect has the exact asymptotic

\[
\boxed{
\frac{\kappa_{A,c}(s_A)-\kappa_P(s_A)}
{\kappa_P(s_A)}
\longrightarrow
-\frac{c-1}{k+c-1}.
}
\tag{3}
\]

Consequently,

\[
\boxed{
\liminf_{A\to\infty}
\sup_{s>1}
\frac{|\kappa_{A,c}(s)-\kappa_P(s)|}
{\kappa_P(s)}
\ge
\frac{c-1}{k+c-1}>0.
}
\tag{4}
\]

Thus the full relative-curvature topology that is blind to the sublinear transports of AF-514 is **not** blind to this proportional tail transport. Linear-scale displacement has a nonvanishing witness at a mesoscopic point approaching the convergence boundary.

The effect is not ordinary dilation sensitivity. If every prime were replaced by `cp`, then the Dirichlet sum would be exactly `c^{-s}P(s)` and the curvature would be unchanged, as classified in AF-509--AF-510. The gap in `(3)` is created by the **interface between an undilated growing prefix and a dilated cofinite tail**.

## Derivation

Put

\[
S_A(s)=\sum_{p\le A}p^{-s},
\qquad
T_A(s)=P(s)-S_A(s).
\tag{5}
\]

The control source has Dirichlet sum

\[
P_{A,c}(s)
=S_A(s)+c^{-s}T_A(s)
=c^{-s}P(s)+(1-c^{-s})S_A(s).
\tag{6}
\]

Define

\[
a(s)=c^{-s},
\qquad
r_A(s)=\frac{S_A(s)}{P(s)},
\qquad
F_A(s)=a(s)+(1-a(s))r_A(s).
\tag{7}
\]

Then

\[
P_{A,c}(s)=P(s)F_A(s)
\]

and therefore

\[
\kappa_{A,c}(s)-\kappa_P(s)
=(\log F_A)''(s).
\tag{8}
\]

The problem is reduced to the behavior of the retained-prefix fraction `r_A` on the scale `(2)`.

### 1. The prime sum and the retained prefix occupy fixed proportions on the mesoscopic scale

Write

\[
L=\log A,
\qquad
\ell=\log L,
\qquad
t=L^{-k},
\qquad s=1+t.
\tag{9}
\]

The classical prime-zeta relation

\[
P(s)=\sum_{m\ge1}\frac{\mu(m)}m\log\zeta(ms)
\tag{10}
\]

shows that only the `m=1` term is singular at `s=1`. Hence, as `t\downarrow0`,

\[
P(1+t)=\log\frac1t+O(1),
\tag{11}
\]

\[
P'(1+t)=-\frac1t+O(1),
\qquad
P''(1+t)=\frac1{t^2}+O(1).
\tag{12}
\]

At the chosen scale, `(11)` gives

\[
P(s_A)=k\ell+O(1).
\tag{13}
\]

On the other hand, Mertens' prime reciprocal estimate and the standard weighted prime sums give

\[
\sum_{p\le A}\frac1p=\ell+O(1),
\tag{14}
\]

\[
\sum_{p\le A}\frac{\log p}{p}=O(L),
\qquad
\sum_{p\le A}\frac{(\log p)^2}{p}=O(L^2).
\tag{15}
\]

Since `1-e^{-x}\le x` for `x\ge0`,

\[
0\le
\sum_{p\le A}\frac1p-S_A(1+t)
\le
t\sum_{p\le A}\frac{\log p}{p}
=O(L^{1-k})=o(1).
\tag{16}
\]

Therefore

\[
S_A(s_A)=\ell+O(1)
\tag{17}
\]

and

\[
\boxed{
r_A(s_A)\longrightarrow\frac1k.}
\tag{18}
\]

The condition `k>1` is exactly what makes the retained cutoff `A` negligible on the derivative scale while leaving it as a fixed fraction of the logarithmic divergence itself.

### 2. The second derivative of the prefix fraction carries a fixed negative share of prime curvature

Let

\[
u(s)=\frac{P'(s)}{P(s)}=(\log P)'(s),
\qquad
\kappa(s)=\kappa_P(s).
\tag{19}
\]

From `(12)`--`(13)`, at `s=s_A`,

\[
u(s_A)
\sim
-\frac1{k t\ell},
\tag{20}
\]

and

\[
\kappa(s_A)
=
\frac{P''}{P}-u^2
\sim
\frac1{k t^2\ell}.
\tag{21}
\]

In particular,

\[
\frac{u(s_A)^2}{\kappa(s_A)}
=O\!\left(\frac1\ell\right)
\longrightarrow0.
\tag{22}
\]

Differentiate `r_A=S_A/P`:

\[
r_A'
=\frac{S_A'}P-r_Au,
\tag{23}
\]

\[
r_A''
=\frac{S_A''}P
-2\frac{S_A'}P u
+r_Au^2
-r_A\kappa.
\tag{24}
\]

Equation `(15)` gives at `s_A`

\[
|S_A'(s_A)|=O(L),
\qquad
S_A''(s_A)=O(L^2).
\tag{25}
\]

Using `(13)`, `(20)`--`(21)`, and `t=L^{-k}`,

\[
\frac{S_A''/P}{\kappa}
=O(L^2t^2)
=O(L^{2-2k})
\longrightarrow0,
\tag{26}
\]

and

\[
\frac{|(S_A'/P)u|}{\kappa}
=O\!\left(\frac{Lt}{\ell}\right)
=O\!\left(\frac{L^{1-k}}\ell\right)
\longrightarrow0.
\tag{27}
\]

Combining `(18)`, `(22)`, and `(24)`--`(27)` yields

\[
\boxed{
\frac{r_A''(s_A)}{\kappa(s_A)}
\longrightarrow-rac1k.}
\tag{28}
\]

Equation `(23)` also gives

\[
r_A'(s_A)=O\!\left(\frac1{t\ell}\right),
\]

so

\[
\boxed{
\frac{r_A'(s_A)^2}{\kappa(s_A)}
=O\!\left(\frac1\ell\right)
\longrightarrow0.}
\tag{29}
\]

Thus the first derivative is negligible at the curvature scale, while the second derivative retains a finite fraction of that scale.

### 3. The prefix-tail interface produces the explicit curvature gap

From `(7)`,

\[
F_A'
=a'(1-r_A)+(1-a)r_A',
\tag{30}
\]

\[
F_A''
=a''(1-r_A)-2a'r_A'+(1-a)r_A''.
\tag{31}
\]

At `s_A\to1`,

\[
a(s_A)\to a_0:=\frac1c,
\tag{32}
\]

while `a'` and `a''` remain bounded. Equations `(21)`, `(28)`, and `(29)` therefore imply

\[
\frac{F_A''(s_A)}{\kappa(s_A)}
\longrightarrow
-\frac{1-a_0}{k},
\tag{33}
\]

and

\[
\frac{F_A'(s_A)^2}{\kappa(s_A)}
\longrightarrow0.
\tag{34}
\]

By `(18)` and `(32)`,

\[
F_A(s_A)
\longrightarrow
F_0
=
\frac1c+\left(1-\frac1c\right)\frac1k
=
\frac{k+c-1}{ck}.
\tag{35}
\]

Since

\[
(\log F_A)''
=\frac{F_A''}{F_A}
-\frac{F_A'^2}{F_A^2},
\tag{36}
\]

substitution of `(33)`--`(35)` gives

\[
\frac{(\log F_A)''(s_A)}{\kappa(s_A)}
\longrightarrow
-\frac{(1-1/c)/k}{(k+c-1)/(ck)}
=-\frac{c-1}{k+c-1}.
\tag{37}
\]

Equation `(8)` proves `(3)`, and evaluating the supremum in `(4)` at `s=s_A` proves `(4)`.

Equivalently, the control curvature itself satisfies

\[
\boxed{
\frac{\kappa_{A,c}(s_A)}{\kappa_P(s_A)}
\longrightarrow
\frac{k}{k+c-1}.}
\tag{38}
\]

The positive limit confirms that `(3)` is a genuine finite relative defect, not a sign pathology of the logarithmic-curvature representation.

## Fidelity and matched-control audit

The family `(1)` is deliberately close to the AF-514 controls in source semantics while crossing their transport scale:

- the full prime prefix below `A` is retained exactly;
- the moved tail remains infinite and simple;
- every moved generator is an ordinary composite integer;
- the displacement is
  \[
  h_p=(c-1)p,
  \]
  so it is proportional rather than sublinear;
- the observation remains the same full relative-curvature carrier used in AF-511--AF-514.

For `c=2`, one has `h_p=p`, exactly at the linear edge of AF-514's comparability range `0\le h_p\le p`. Its weighted transport budget would contain

\[
\sum_{p>A}\frac{1+\log^2p}{p},
\]

which diverges, so AF-514 makes no invisibility prediction for this family. The present result therefore does not contradict AF-514; it supplies a positive witness on the first natural scale beyond its vanishing-budget examples.

The global-dilation control is equally important. If the prefix in `(1)` were also multiplied by `c`, then

\[
P_{c\mathbb P}(s)=c^{-s}P(s)
\]

and

\[
\kappa_{c\mathbb P}(s)=\kappa_P(s)
\]

exactly. Hence curvature is not detecting the absolute factor `c`. It detects the **relative provenance break** between two source regions that have been put in different dilation gauges.

This makes `(3)` a useful structural discriminator rather than a generic large-perturbation statement: the same dilation is an exact curvature gauge when applied globally and a finite curvature defect when applied only beyond an expanding cutoff.

## Representation audit

The tested representation remains

\[
\|Q-\mathbb P\|_{\mathrm{rel}\,\kappa}
=
\sup_{s>1}
\frac{|\kappa_Q(s)-\kappa_P(s)|}{\kappa_P(s)}.
\tag{39}
\]

AF-514 proves that this topology has zero provenance margin along a large class of sublinear support transports. AF-515 shows that the topology is not indiscriminately weak: a proportional tail transport leaves a nonzero footprint when sampled on the cutoff-adapted scale `(2)`.

The mesoscopic scale has a simple interpretation. At `s_A=1+(\log A)^{-k}`, the prime-zeta divergence has size approximately `k\log\log A`, while the retained prefix contributes approximately `\log\log A`. The prefix therefore occupies the asymptotic fraction `1/k` of the source. Multiplying only the complementary tail by `c^{-s}` changes that mixture by an order-one amount, and its second derivative survives relative to the ambient curvature.

This does **not** establish a complete transport threshold. The weighted condition in AF-514 is sufficient for invisibility, not necessary, and `(3)` treats one highly structured linear family. The durable conclusion is narrower: the frontier between recoverable and unrecoverable provenance is not beyond all growing displacement; at least one canonical linear-scale family is separated with an explicit positive margin.

## Prior art and novelty assessment

No novelty is claimed for the analytic ingredients. The proof uses only classical prime-zeta and Mertens asymptotics plus elementary differentiation.

- C.-E. Fröberg, **“On the prime zeta function,”** *BIT* 8 (1968), 187–202, DOI `10.1007/BF01933420`, is the classical source already used by AF-512--AF-514 for the Möbius relation `(10)` and the logarithmic singularity at `s=1`.
- The prime reciprocal and logarithmically weighted estimates `(14)`--`(15)` are classical Mertens/PNT-level prime-sum estimates obtainable by partial summation from standard prime-counting results.
- AF-509--AF-510 supply the exact dilation-fiber classification and canonical quotient inverse; they are the relevant internal control showing that a common global dilation is invisible to curvature.
- AF-514 supplies the complementary weighted-transport invisibility theorem for a broad sublinear family.

A focused literature search for prime-zeta curvature under an expanding cutoff with a piecewise common dilation did not locate a standard theorem matching the exact asymptotic `(3)`. This finding is nevertheless classified `NO-NOVELTY-CLAIM`: its research value is the explicit threshold witness and the interface mechanism inside the Arithmetic Fidelity program, not a claim of a new general prime-zeta theorem.

## Boundaries and failure modes

1. **This is a witness, not a necessary-and-sufficient threshold theorem.** The result proves visibility for the specific proportional family `(1)` and does not classify arbitrary `h_p=\Theta(p)` transports.
2. **The cutoff-adapted observation is essential to the proof.** Equation `(3)` is established at `s_A=1+(\log A)^{-k}` with fixed `k>1`; it does not claim a comparable defect at every fixed `s>1`.
3. **The condition `k>1` is load bearing.** It ensures `t_A\log A\to0`, so the prefix derivative terms are negligible relative to prime curvature while the prefix mass remains a fixed fraction of the logarithmic divergence.
4. **Integer `c\ge2` is chosen to give an exact ordinary-composite matched control.** The analytic calculation extends formally to other positive dilation factors, but those controls need not remain in the positive-integer source class.
5. **Global dilation remains an exact gauge.** The theorem detects the prefix-tail interface, not an absolute scale that curvature intrinsically remembers.
6. **No RH consequence follows.** The result classifies one stability boundary of a prime-derived compression; it does not transfer zeta zeros or establish an RH-equivalent discriminator.

## Consequence for the line

AF-511--AF-514 progressively showed that remote finite changes, the convergence boundary, cofinite fixed shifts, and even unbounded sublinear tail transports can all have vanishing relative-curvature distance from the prime source. AF-515 supplies the first clean counterweight: a cofinite **linear-scale** tail transport is separated by a fixed positive relative-curvature defect.

The next useful question is now sharper than simply asking for a stronger source-aware observable. One can ask for the actual boundary between the two regimes: for displacement laws `h_p` between `o(p)` and `\Theta(p)`, which transport functionals are necessary or sufficient for a nonzero curvature margin, and can that boundary be expressed intrinsically rather than through the sufficient budget of AF-514? A successful answer would turn the present sublinear-versus-linear contrast into a genuine stability classification rather than a pair of examples.