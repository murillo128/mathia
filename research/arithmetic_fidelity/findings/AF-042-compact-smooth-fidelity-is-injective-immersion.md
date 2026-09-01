# AF-042 — Compact smooth fidelity is exactly injective immersion

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `STRUCTURAL-CLASSIFICATION`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `(M,g)` be a compact connected smooth Riemannian manifold, with or without boundary, and let

\[
F:M\to\mathbb R^q
\]

be `C^1`. Define the global lower fidelity modulus

\[
\beta(F)
=
\inf_{x\ne y}
\frac{\|F(x)-F(y)\|}{d_M(x,y)}.
\]

Because `M` is compact, every `C^1` map is globally Lipschitz for `d_M`. Then:

1. **Stable fidelity is exactly global injectivity plus first-order fidelity.**
   \[
   \boxed{
   \beta(F)>0
   \iff
   F\text{ is an injective immersion}.
   }
   \]
   Equivalently, on a compact smooth carrier, a `C^1` representation is bi-Lipschitz onto its image exactly when it has no global collisions and no infinitesimal kernel.

2. **For a smooth compression chain, the two gates have a direct geometric form.** Let
   \[
   A:M\to\mathbb R^n,
   \qquad
   B:U\subseteq\mathbb R^n\to\mathbb R^q,
   \qquad
   A(M)\subseteq U,
   \]
   be `C^1`, with `A` an immersion, and put `F=B\circ A`. Then
   \[
   dF_x\text{ is injective}
   \iff
   dA_x(T_xM)\cap\ker dB_{A(x)}=\{0\}.
   \]
   Hence
   \[
   \boxed{
   \beta(B\circ A)>0
   \iff
   \begin{cases}
   B\circ A\text{ is globally injective},\\
   dA_x(T_xM)\cap\ker dB_{A(x)}=\{0\}
   \text{ for every }x\in M.
   \end{cases}}
   \]

3. **Compactness converts pointwise local fidelity into a uniform stability margin, but only after the global collision gate is passed.** If `F` is an injective immersion, the smallest singular value of `dF_x` is positive at every point and therefore has a positive compact minimum. Local inverse charts give a uniform short-range lower Lipschitz bound; injectivity plus compactness gives a separate positive long-range secant separation. The global modulus is the minimum of those two mechanisms.

4. **The compactness conclusion is not available in noncompact or asymptotic limits.** There are injective smooth immersions with a uniform derivative lower bound but `\beta(F)=0`. In particular, for irrational `\alpha`,
   \[
   F_\alpha(t)
   =
   (\cos t,\sin t,\cos(\alpha t),\sin(\alpha t))
   \in\mathbb R^4
   \]
   is injective and satisfies
   \[
   \|F_\alpha'(t)\|=\sqrt{1+\alpha^2}
   \qquad\text{for all }t,
   \]
   yet `\beta(F_\alpha)=0`.

5. **Finite compact truncations can therefore be individually stable while losing every uniform margin.** Each restriction of `F_\alpha` to a compact interval is an injective immersion and hence has positive lower fidelity modulus, but there is an increasing sequence of compact intervals whose moduli tend to zero. Thus finite-stage compactness cannot replace a uniform asymptotic secant audit.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{on compact smooth carriers, stable fidelity = global secant injectivity + tangent fidelity; outside compactness, those gates need a separate uniformity condition.}
}
\]

This joins AF-001's exact fiber criterion, AF-007's infinitesimal vertical criterion, and AF-041's range–kernel stability geometry into one finite-dimensional smooth classification.

## Derivation

### Stable fidelity forces injective immersion

Assume `\beta(F)>0`. Then for `x\ne y`,

\[
\|F(x)-F(y)\|
\ge
\beta(F)d_M(x,y)>0,
\]

so `F` is injective.

Let `x\in M` and `v\in T_xM`. Choose a smooth curve `c` in `M` with

\[
c(0)=x,
\qquad
c'(0)=v.
\]

Using a Riemannian normal chart when `x` is interior, and an inward local chart at a boundary point, one may choose the curve so that

\[
d_M(c(t),x)=|t|\,\|v\|+o(|t|).
\]

The lower Lipschitz inequality gives

\[
\frac{\|F(c(t))-F(x)\|}{|t|}
\ge
\beta(F)
\frac{d_M(c(t),x)}{|t|}.
\]

Taking `t\to0` yields

\[
\|dF_x(v)\|
\ge
\beta(F)\|v\|.
\]

Thus `dF_x` is injective at every point. In fact the global lower modulus already gives a uniform differential lower bound.

### Injective immersion gives a uniform local lower bound

Now assume `F` is an injective immersion.

By the immersion theorem, for every `x\in M` there is a neighborhood `U_x` on which `F` is a `C^1` embedding into a smooth embedded submanifold of `\mathbb R^q`. In adapted coordinates the map has the local normal form

\[
u\longmapsto (u,0),
\]

up to `C^1` coordinate changes. The local inverse on the image is therefore `C^1`, hence locally Lipschitz.

After shrinking the neighborhoods, for each `x` there are constants `r_x>0` and `c_x>0` such that

\[
\|F(y)-F(z)\|
\ge
c_x d_M(y,z)
\]

whenever `y,z` lie in the chosen neighborhood and are sufficiently close.

Compactness supplies a finite subcover and a Lebesgue number. Therefore there exist uniform constants

\[
r>0,
\qquad
c_{\mathrm{loc}}>0
\]

such that

\[
d_M(y,z)<r
\quad\Longrightarrow\quad
\|F(y)-F(z)\|
\ge
c_{\mathrm{loc}}d_M(y,z).
\]

Equivalently, the local inverse conditioning cannot drift to zero on a fixed compact carrier.

The same conclusion is visible directly from the differential. The unit tangent bundle is compact and

\[
(x,v)\longmapsto \|dF_x(v)\|
\]

is continuous and strictly positive on unit tangent vectors, so

\[
m_0
=
\min_{\substack{x\in M\\\|v\|=1}}
\|dF_x(v)\|
>0.
\]

The local chart argument is the nonlinear step converting this uniform tangent lower bound into a lower bound on sufficiently short secants.

### Injectivity and compactness control long secants

Local immersion information says nothing by itself about distant points folding onto one another. Injectivity handles that second gate.

For the uniform radius `r` above, consider

\[
K_r
=
\{(x,y)\in M\times M:d_M(x,y)\ge r\}.
\]

This is compact. Since `F` is injective, the continuous function

\[
(x,y)\longmapsto\|F(x)-F(y)\|
\]

is strictly positive on `K_r`. Hence

\[
\delta_r
=
\min_{K_r}\|F(x)-F(y)\|>0.
\]

Let `D=\operatorname{diam}(M)`. For every pair with `d_M(x,y)\ge r`,

\[
\frac{\|F(x)-F(y)\|}{d_M(x,y)}
\ge
\frac{\delta_r}{D}.
\]

Combining short and long pairs gives

\[
\boxed{
\beta(F)
\ge
\min\left(c_{\mathrm{loc}},\frac{\delta_r}{D}\right)
>0.
}
\]

The upper Lipschitz bound is classical: compactness gives

\[
L=\max_{\substack{x\in M\\\|v\|=1}}\|dF_x(v)\|<\infty,
\]

and integrating `dF` along minimizing curves gives

\[
\|F(x)-F(y)\|\le Ld_M(x,y).
\]

Thus `F` is bi-Lipschitz onto its image.

The proof isolates two genuinely different stability mechanisms:

\[
\text{short secants}
\longleftrightarrow
\text{immersion / tangent survival},
\]

\[
\text{long secants}
\longleftrightarrow
\text{global injectivity / self-separation}.
\]

Neither can replace the other.

## Composition form: tangent range versus downstream kernel

Let `F=B\circ A` with `A` an immersion. By the chain rule,

\[
dF_x
=
dB_{A(x)}\circ dA_x.
\]

Because `dA_x` is injective,

\[
\begin{aligned}
dF_x(v)=0
&\iff
dA_x(v)\in\ker dB_{A(x)}\\
&\iff
dA_x(v)\in dA_x(T_xM)\cap\ker dB_{A(x)}.
\end{aligned}
\]

Therefore

\[
\boxed{
F\text{ is an immersion}
\iff
dA_x(T_xM)\cap\ker dB_{A(x)}=\{0\}
\text{ for every }x.
}
\]

This is the nonlinear finite-dimensional analogue of AF-041's range–kernel intersection gate. On a compact carrier, once this pointwise tangent gate and global injectivity both hold, no extra hidden finite-scale conditioning hypothesis is needed: compactness forces a positive minimum secant modulus.

That statement is deliberately finite-dimensional and compact. AF-041 shows why one cannot export it naively to infinite-dimensional operator chains, where a trivial range–kernel intersection may coexist with zero angle and nonclosed range.

## Boundary controls

### Exact global fidelity can fail first-order stability

On the compact interval

\[
M=[-1,1],
\qquad
F(t)=t^3,
\]

`F` is injective, so there are no exact global collisions. But

\[
F'(0)=0,
\]

and

\[
\frac{|F(t)-F(0)|}{|t|}=t^2\to0.
\]

Hence `\beta(F)=0`. Exact fiber fidelity alone does not imply stable smooth fidelity.

### Perfect tangent fidelity can fail the global collision gate

For

\[
F:S^1\to S^1\subset\mathbb R^2,
\qquad
F(z)=z^2,
\]

`F` is a local diffeomorphism and its derivative never vanishes, but it is two-to-one. Thus tangent fidelity cannot detect discrete sheet identification, exactly as AF-007's double-cover control already showed for discriminator descent.

### Noncompact exact immersions can be arbitrarily unstable

Fix irrational `\alpha` and define

\[
F_\alpha(t)
=
(\cos t,\sin t,\cos(\alpha t),\sin(\alpha t)).
\]

If `F_\alpha(t)=F_\alpha(s)`, then

\[
t-s=2\pi k,
\qquad
\alpha(t-s)=2\pi m
\]

for integers `k,m`. Irrationality forces `k=m=0`, hence `t=s`. So `F_\alpha` is injective.

Moreover

\[
\|F_\alpha'(t)\|^2
=1+\alpha^2,
\]

so the derivative has a constant positive lower bound.

Nevertheless Dirichlet approximation gives infinitely many integers `q\ge1` and `p` such that

\[
|q\alpha-p|<\frac1q.
\]

Set

\[
t_q=2\pi q.
\]

Then the first circle coordinate of `F_\alpha(t_q)` equals that of `F_\alpha(0)`, while

\[
\begin{aligned}
\|F_\alpha(t_q)-F_\alpha(0)\|
&=
|e^{2\pi i q\alpha}-1|\\
&=
|e^{2\pi i(q\alpha-p)}-1|\\
&\le
2\pi|q\alpha-p|\\
&<\frac{2\pi}{q}.
\end{aligned}
\]

Since `|t_q|=2\pi q`,

\[
\frac{\|F_\alpha(t_q)-F_\alpha(0)\|}{|t_q|}
<\frac1{q^2}\to0.
\]

Therefore

\[
\boxed{\beta(F_\alpha)=0.}
\]

This example is stronger than a mere global collision: **exact injectivity and uniformly nondegenerate local differential information both survive, while global stable recoverability fails through recurrence.**

## Finite-stage consequence

Let

\[
I_Q=[-2\pi Q,2\pi Q].
\]

For every finite `Q`, the restriction

\[
F_\alpha|_{I_Q}:I_Q\to\mathbb R^4
\]

is a `C^\infty` injective immersion on a compact carrier, so the theorem gives

\[
\beta_Q>0.
\]

Choose the Dirichlet denominators `q_j\to\infty` above and take `Q_j=q_j`. Then both `0` and `t_{q_j}=2\pi q_j` lie in `I_{Q_j}`, giving

\[
0<\beta_{Q_j}
\le
\frac{\|F_\alpha(t_{q_j})-F_\alpha(0)\|}{|t_{q_j}|}
<\frac1{q_j^2}.
\]

Hence

\[
\boxed{\beta_{Q_j}\to0.}
\]

Every finite truncation is stably faithful, and the tangent lower bound is the same at every scale, yet the family has no uniform inverse condition number. The failure lives entirely in long-range secants created by recurrence.

For Mathia this is the decisive asymptotic warning: proving an injective immersion separately at every finite cutoff does not justify a limiting fidelity claim. A scale-uniform theorem must also control long-range self-approach of the retained representation.

## Prior art and novelty assessment

The differential-topological ingredients are classical and no novelty is claimed for the compact injective-immersion theorem, local embedded normal form, or Diophantine recurrence.

- John M. Lee, ***Introduction to Smooth Manifolds***, 2nd ed., Graduate Texts in Mathematics 218, Springer (2012), DOI `10.1007/978-1-4419-9982-5`, especially Proposition 4.22. Role: an injective smooth immersion is an embedding when the source is compact; the immersion theorem supplies the local embedded normal form used in the short-secant argument.
- Hossein Movahedi-Lankarani and Robert Wells, **“On geometric quotients,”** *Annales Academiae Scientiarum Fennicae Mathematica* 34 (2009), 3–26. Role: close prior art relating `C^1` quotient/embedding structure on compact manifolds to Lipschitz and bi-Lipschitz metric structure; it confirms that smooth-versus-metric recoverability on compact geometric quotients is an established mathematical theme rather than a new Arithmetic Fidelity theorem.
- J. W. S. Cassels, ***An Introduction to Diophantine Approximation***, Cambridge Tracts in Mathematics and Mathematical Physics 45, Cambridge University Press (1957), Chapter I. Role: classical Dirichlet approximation theorem used to produce recurrent long secants for the irrational torus flow.

The exact equivalence

\[
\beta(F)>0
\iff
F\text{ injective immersion}
\]

is a direct compactness synthesis of standard local differential topology, compact separation, and elementary Lipschitz estimates. It should be treated as classical/derived structure, not a novelty claim.

The Arithmetic Fidelity contribution is the **two-gate organization and asymptotic boundary**:

\[
\text{global secant gate}
+
\text{tangent gate}
\xRightarrow[\text{compact source}]{}
\text{stable recovery},
\]

while the irrational-flow control proves that the implication loses its uniform content once compactness is replaced by an expanding family or noncompact limit. That distinction is directly reusable when a Mathia mechanism is validated only on finite truncations.

## Boundaries and failure modes

- The theorem is metric-relative: `\beta(F)` uses the chosen Riemannian distance on `M` and Euclidean norm on the destination. On one fixed compact manifold all smooth Riemannian metrics are bi-Lipschitz equivalent, but asymptotic families with changing metrics require separate uniform control.
- Compactness is used twice: to uniformize local inverse conditioning and to separate distant image pairs. Pointwise immersion plus injectivity does not supply either global uniformity on a noncompact family.
- Global injectivity is essential. A local diffeomorphism or immersion can erase a discrete sheet label while every differential test passes.
- Immersion is essential. A compact injective `C^1` map can have cusp-like or flat points with vanishing lower secant modulus.
- The composition criterion assumes `A` is already an immersion. If upstream tangent information was lost before `B`, the later range–kernel test cannot restore it.
- The theorem concerns the full vector representation `F(x)`. Any further scalarization, norm, Gram map, spectrum, trace, determinant, or moment summary is a new compression and needs its own fidelity audit.
- For infinite-dimensional carriers the compact finite-dimensional argument does not replace the closed-range/Friedrichs-angle conditions of AF-039 through AF-041.

## Consequences for the line

1. AF-001 and AF-007 now have a stable compact synthesis: **fiber separation plus infinitesimal separation is sufficient for bi-Lipschitz recoverability on a fixed compact smooth carrier**.
2. AF-041's range–kernel transversality becomes the tangent gate for nonlinear smooth compositions. In finite-dimensional compact settings, pointwise immersion automatically acquires a uniform local margin; the remaining independent problem is global self-separation.
3. Any finite-cutoff RH construction should record a scale-dependent lower fidelity modulus rather than treating finite injective-immersion status as an asymptotic certificate. A sequence of positive moduli can converge to zero even when every tangent lower bound is uniform.
4. Recurrent or almost-periodic representations are a particularly sharp stress test: they can preserve local differential information perfectly while producing arbitrarily close long-range secants. Such recurrence must be ruled out or quantitatively controlled before a limiting representation can be called stably arithmetic-faithful.
5. The next useful generalization is not another local rank criterion but a category-appropriate **uniform secant/properness condition** for noncompact or asymptotic carriers, with explicit controls showing when long-range recurrence can or cannot be excluded.