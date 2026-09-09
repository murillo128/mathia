# AF-218 — full Euler log is strictly sign-regular of order two

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `FINITE-ORDER-POSITIVE-GATE`, `SOURCE-COMPLEXITY-GATE`, `EXACT-FIDELITY`, `CLASSICAL-BRIDGE`, `NO-NOVELTY-CLAIM`

## Claim

AF-217 proves that the full Euler-log kernel cannot be totally nonnegative at **all** orders. The first nontrivial finite order nevertheless survives exactly.

Put

\[
L(x):=-\log(1-e^{-x}),\qquad x>0,
\tag{1}
\]

and in logarithmic coordinates define

\[
K(u,v):=L(e^{u-v}).
\tag{2}
\]

Then `K` is **strictly totally positive of order two**: for every

\[
u_1<u_2,\qquad v_1<v_2,
\tag{3}
\]

one has

\[
\boxed{
\det[K(u_i,v_j)]_{i,j=1}^2>0.
}
\tag{4}
\]

Equivalently, in the original Euler variables, for every

\[
0<s_1<s_2,\qquad 1<q_1<q_2,
\tag{5}
\]

one has the strict checkerboard sign

\[
\boxed{
\det\!\begin{pmatrix}
-\log(1-q_1^{-s_1}) & -\log(1-q_2^{-s_1})\\
-\log(1-q_1^{-s_2}) & -\log(1-q_2^{-s_2})
\end{pmatrix}<0.
}
\tag{6}
\]

Thus the first bad order whose existence is guaranteed by AF-217 is **at least three**.

There is also an exact source-complexity consequence. Let

\[
1<q_1<\cdots<q_n
\]

and let `a_1,\ldots,a_n` be nonzero real coefficients. Define

\[
G(s):=\sum_{j=1}^n a_j\big[-\log(1-q_j^{-s})\big].
\tag{7}
\]

If two distinct positive real samples vanish,

\[
G(s_1)=G(s_2)=0,
\qquad 0<s_1<s_2,
\tag{8}
\]

then the ordered coefficient sequence has at least two sign changes:

\[
\boxed{V(a_1,\ldots,a_n)\ge2.}
\tag{9}
\]

Consequently, a nonzero full-Euler signed source with at most one ordered sign change is exactly separated from zero by **any two distinct positive real Euler samples**. This applies in particular when all `q_j` are rational primes.

The result is qualitative globally. Its strictness has a quantitative modulus on compact logarithmic windows, but that modulus degenerates in the small-`s\log q` tail. Therefore AF-218 supplies a genuine finite-order full-Euler gate without contradicting either AF-213's conditioning collapse or AF-217's all-order obstruction.

## Derivation

### 1. The Euler-log profile is strictly log-concave in logarithmic scale

Let

\[
f(t):=L(e^t),
\qquad
 g(t):=\log f(t),
\qquad t\in\mathbb R.
\tag{10}
\]

For `x>0`,

\[
L'(x)=-\frac1{e^x-1}.
\tag{11}
\]

Introduce

\[
A(x):=(e^x-1)L(x)>0.
\tag{12}
\]

Then, with `x=e^t`,

\[
g'(t)
=\frac{xL'(x)}{L(x)}
=-\frac{x}{A(x)}.
\tag{13}
\]

The elementary Euler-log expansion gives an exact useful form for `A`:

\[
\begin{aligned}
A(x)
&=(e^x-1)\sum_{m\ge1}\frac{e^{-mx}}m\\
&=1-\sum_{n\ge1}\frac{e^{-nx}}{n(n+1)}.
\end{aligned}
\tag{14}
\]

Hence

\[
A(0+)=0,
\qquad
A'(x)=\sum_{n\ge1}\frac{e^{-nx}}{n+1}>0,
\tag{15}
\]

and

\[
A''(x)
=-\sum_{n\ge1}\frac{n}{n+1}e^{-nx}<0.
\tag{16}
\]

So `A` is strictly concave on `(0,\infty)` and vanishes at the left endpoint. Strict concavity implies

\[
A(x)-xA'(x)>0,
\tag{17}
\]

or equivalently

\[
\left(\frac{x}{A(x)}\right)'
=\frac{A(x)-xA'(x)}{A(x)^2}>0.
\tag{18}
\]

Differentiating `(13)` with respect to `t` therefore gives

\[
\boxed{
g''(t)
=-x\frac{A(x)-xA'(x)}{A(x)^2}<0,
\qquad x=e^t.
}
\tag{19}
\]

Thus `f(t)=L(e^t)` is strictly log-concave on the whole real line.

If one wants the standard integrable Pólya-frequency normalization, fix any `alpha>0` and put

\[
f_\alpha(t):=e^{\alpha t}f(t).
\tag{20}
\]

As in AF-217, `f_alpha` is integrable. Multiplication by the exponential tilt adds only the affine term `alpha t` to `log f`, so `(19)` is unchanged. It also multiplies translation-kernel rows and columns by positive factors, hence does not change finite-minor signs.

### 2. Strict log-concavity gives every `2 x 2` translation minor the correct sign

Fix `delta>0` and define

\[
R_\delta(t):=\frac{f(t+\delta)}{f(t)}.
\tag{21}
\]

By `(19)`, `g'` is strictly decreasing, so

\[
\frac{d}{dt}\log R_\delta(t)
=g'(t+\delta)-g'(t)<0.
\tag{22}
\]

Therefore `R_delta` is strictly decreasing.

Now let `u_1<u_2` and `v_1<v_2`. Set

\[
a:=u_1-v_2,
\qquad
c:=u_2-v_2,
\qquad
\delta:=v_2-v_1.
\tag{23}
\]

Then `a<c`, `delta>0`, and

\[
\begin{aligned}
\det[K(u_i,v_j)]_{i,j=1}^2
&=f(a+\delta)f(c)-f(a)f(c+\delta)\\
&=f(a)f(c)\big(R_\delta(a)-R_\delta(c)\big)>0.
\end{aligned}
\tag{24}
\]

This proves `(4)` directly. In classical language, an exponential tilt of `f` is a strict Pólya-frequency function of order two, and the translation kernel is `STP_2`.

### 3. Increasing generator norms reverse the source coordinate

For the Euler factor set

\[
v_q:=-\log\log q.
\tag{25}
\]

Then

\[
K(\log s,v_q)
=L(s\log q)
=-\log(1-q^{-s}).
\tag{26}
\]

If `q_1<q_2`, then

\[
v_{q_1}>v_{q_2}.
\tag{27}
\]

Thus increasing generator norm reverses the `v`-column order. Applying `(4)` to the increasing pair `(v_{q_2},v_{q_1})` and then swapping the two columns gives exactly `(6)`.

This is the order-two instance of the checkerboard factor in AF-217: for `n=2`,

\[
(-1)^{n(n-1)/2}=-1,
\]

and `(6)` says that the corrected minor is strictly positive.

### 4. Two full-Euler samples detect every source with at most one sign change

Define

\[
E_s(q):=-\log(1-q^{-s})>0.
\tag{28}
\]

For fixed `0<s_1<s_2`, equation `(6)` implies that the ratio

\[
r(q):=\frac{E_{s_2}(q)}{E_{s_1}(q)}
\tag{29}
\]

is strictly decreasing in `q>1`. Indeed, for `q_1<q_2`, divide `(6)` by the positive product `E_{s_1}(q_1)E_{s_1}(q_2)` to obtain

\[
r(q_2)<r(q_1).
\tag{30}
\]

Suppose now that `(8)` holds and `V(a)\le1`.

If `V(a)=0`, all coefficients have the same sign after a global sign change, and `(7)` cannot vanish because every kernel value is positive.

If `V(a)=1`, multiply all coefficients by `-1` if necessary. There is then an index `k` such that

\[
a_j>0\quad(j\le k),
\qquad
a_j<0\quad(j>k).
\tag{31}
\]

The first equality in `(8)` gives

\[
\sum_{j\le k}a_jE_{s_1}(q_j)
=
\sum_{j>k}(-a_j)E_{s_1}(q_j)
=:M>0.
\tag{32}
\]

Using the second equality in `(8)` and `(29),`

\[
\sum_{j\le k}a_jE_{s_1}(q_j)r(q_j)
=
\sum_{j>k}(-a_j)E_{s_1}(q_j)r(q_j).
\tag{33}
\]

After division by `M`, `(33)` says that a weighted average of `r(q_j)` over the left block equals a weighted average over the right block. But every left-block norm is smaller than every right-block norm, while `r` is strictly decreasing. Hence every value entering the left average is strictly larger than every value entering the right average, a contradiction.

Therefore `(8)` forces `V(a)\ge2`, proving `(9)`.

This is an exact **full-Euler** analogue of AF-216 at the first nontrivial sign budget. AF-216 works at arbitrary order for the first Dirichlet harmonic; AF-218 shows that the higher Euler harmonics do not destroy the sign-complexity mechanism immediately. They preserve it through order two.

### 5. Strictness has a compact-window quantitative modulus

Equation `(19)` gives an exact curvature

\[
\kappa(t):=-g''(t)
=e^t\frac{A(e^t)-e^tA'(e^t)}{A(e^t)^2}>0.
\tag{34}
\]

For the variables in `(23)`,

\[
\log\frac{R_\delta(a)}{R_\delta(c)}
=
\int_a^c\int_r^{r+\delta}\kappa(z)\,dz\,dr.
\tag{35}
\]

Hence, on any compact logarithmic window containing the integration rectangle, if `kappa_*` is the positive minimum of `kappa`, then

\[
\boxed{
\frac{R_\delta(a)}{R_\delta(c)}
\ge
\exp\!\big(\kappa_*\,\delta(c-a)\big)>1.
}
\tag{36}
\]

So separated sample coordinates and separated source coordinates do yield a uniform order-two determinant margin on compact windows.

There is no global margin of this form. As `t->-infinity`, equivalently `x=e^t->0`,

\[
L(x)\sim\log(1/x),
\qquad
A(x)\sim x\log(1/x),
\]

and `(34)` gives

\[
\kappa(t)\sim\frac1{t^2}\longrightarrow0.
\tag{37}
\]

Thus exact order-two sign regularity can coexist with arbitrarily weak conditioning in the small-`s\log q` regime. This is the same exact-versus-stable distinction emphasized throughout Arithmetic Fidelity.

## Relation to AF-216 and AF-217

AF-216 proves an all-order Chebyshev theorem for the first Dirichlet harmonic: annihilating `m` equally spaced real samples requires at least `m` ordered sign changes.

AF-217 then proves that the complete Euler logarithm cannot inherit that theorem through an all-order total-positivity argument, because its translation kernel fails total nonnegativity at some finite order. The exact first failing order was left open.

AF-218 resolves the first nontrivial case positively:

\[
\boxed{
\text{full Euler log is strictly sign-regular through order }2,
\quad
\text{but not through all orders.}
}
\tag{38}
\]

Therefore the finite-order frontier begins at order three. Any attempt to exploit a source-forced sign budget `r>=2` must determine whether the Euler kernel remains sign-regular through order `r+1`, or replace total positivity by a different source-specific transfer theorem.

## Exact controls and boundaries

### This is not `TP_infinity`

AF-217 remains decisive. AF-218 proves only the `1 x 1` and `2 x 2` signs. It neither proves nor suggests that every `3 x 3` minor has the required sign.

### This is an exact detection theorem, not a global conditioning theorem

Equation `(9)` says that a source with at most one sign change cannot annihilate two distinct real Euler samples exactly. The source may still make both samples arbitrarily small after normalization if source/sample coordinates approach a degeneracy. Equation `(37)` explicitly exhibits one curvature degeneration.

### Primality is not used in the positive theorem

The proof works for arbitrary real `q_j>1`. Prime support is therefore allowed but supplies no extra strength at order two. An RH-facing application still needs a source-forced restriction on the **signed discrepancy**, not merely prime labels on its atoms.

### The source ordering is essential

The sign budget in `(9)` is counted after the supports are merged and ordered by increasing generator norm, exactly as in AF-216. Permuting coefficients independently of their source nodes changes the hypothesis.

### Two samples are sharp for the declared sign class

One positive sample detects sign-constant sources but cannot in general distinguish a one-sign-change signed source: positive and negative blocks can be rescaled to cancel a single scalar observation. AF-218 shows that a second distinct real sample closes that exact collision because the likelihood ratio `(29)` is strictly monotone.

### Compact quantitative margins need geometric separation

The lower margin in `(36)` depends on a compact `u-v` window and on nonzero gaps in both sample and source coordinates. AF-218 does not provide a scale-free lower bound for arbitrarily close generator norms, arbitrarily close samples, or unbounded source families.

## Prior art and novelty assessment

The order-two mechanism is classical total-positivity mathematics, and no novelty is claimed for the equivalence between log-concavity and the `PF_2` property or for its variation-diminishing consequences.

- Samuel Karlin, ***Total Positivity, Vol. I***, Stanford University Press (1968), is the classical systematic reference for totally positive kernels, Pólya-frequency functions, monotone likelihood ratios, and variation-diminishing arguments.
- Adrien Saumard and Jon A. Wellner, **"Log-Concavity and Strong Log-Concavity: a review,"** *Statistics Surveys* **8** (2014), 45--114, DOI `10.1214/14-SS107`. Proposition 2.3 records the classical equivalence between one-dimensional log-concave functions and Pólya-frequency functions of order two.
- I. J. Schoenberg's Pólya-frequency papers cited in AF-217 supply the foundational finite-minor/translation-kernel language. AF-217 uses his `PF_infinity` Laplace-transform theorem for the all-order obstruction; AF-218 uses only the elementary order-two side.
- Apoorva Khare, **"Multiply positive functions, critical exponent phenomena, and the Jain-Karlin-Schoenberg kernel,"** arXiv:`2008.05121` (2020), gives modern finite-order multiply-positive context and emphasizes that finite `PF_p` behavior is genuinely weaker than `PF_infinity`.
- Olga M. Katkova, **"Multiple Positivity and the Riemann Zeta-Function,"** *Computational Methods and Function Theory* **7** (2007), DOI `10.1007/BF03321628`, is direct prior art that finite/multiple positivity and the zeta problem have already been studied together, although in a different generating-function setting.

The strict log-concavity calculation `(14)`--`(19)` and its exact Euler-factor specialization were derived directly here. A targeted search did not locate this precise `L(e^t)` order-two statement, but absence of a located source is not evidence of novelty. The durable contribution should be read conservatively as the exact placement of the classical `PF_2` gate inside the AF-216/AF-217 obstruction chain.

## Consequence for the Arithmetic Fidelity frontier

The all-or-nothing question left by AF-217 is now narrowed. The full Euler aggregation preserves ordered-sign information at the first nontrivial finite level: one sign change cannot hide from two positive real samples. The failure of total positivity occurs later.

The next exact question is therefore **order three**. Determine whether the Euler-log translation kernel is sign-regular of order three, and if so continue only as far as the finite-order signs survive. In parallel, any proposed arithmetic application must derive an actual sign-complexity bound for its prime-derived signed source and combine it with a quantitative modulus in the relevant `s\log q` window. Without both a source-side oscillation law and an observation-side finite-order margin, exact sign regularity alone is not a stable RH-facing mechanism.