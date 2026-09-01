# AF-037 — Bounded multiplicative channel degree is exactly interaction cover number

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`

## Claim

Let

\[
(X_i,\Sigma_i,q_i),\qquad i=1,\ldots,d,
\]

be probability spaces, let

\[
Q=\bigotimes_{i=1}^d q_i,
\]

and use the product-space Hoeffding decomposition from AF-034,

\[
L^2(Q)=\bigoplus_{S\subseteq[d]}\mathcal H_S.
\]

Fix a finite family of retained coordinate channels

\[
\mathcal A=\{A_1,\ldots,A_m\},\qquad A_j\subseteq[d],
\]

write

\[
\mathcal F_{A_j}=\sigma(X_i:i\in A_j),
\qquad
V_{A_j}=L^2(\mathcal F_{A_j}),
\]

and put

\[
U=\bigcup_{j=1}^m A_j.
\]

For each coordinate support `S\subseteq[d]`, define its **channel cover number**

\[
\kappa_{\mathcal A}(S)
=
\min\left\{
|I|:
I\subseteq[m],\
S\subseteq\bigcup_{j\in I}A_j
\right\},
\]

with `\kappa_{\mathcal A}(\varnothing)=0` and `\kappa_{\mathcal A}(S)=\infty` if `S\not\subseteq U`.

For `r\ge0`, define the bounded multiplicative channel-degree space

\[
W_r
=
\overline{\operatorname{span}}^{\,L^2(Q)}
\left\{
\prod_{\ell=1}^{k} f_\ell:
0\le k\le r,\
f_\ell\in L^\infty(\mathcal F_{A_{j_\ell}})
\right\},
\]

where the empty product is `1`. Repeated channel indices are allowed; they never improve the cover number because a product of functions measurable with respect to the same channel is still measurable with respect to that channel.

Then:

1. **Exact cover-number filtration.**
   \[
   \boxed{
   W_r
   =
   \bigoplus_{\kappa_{\mathcal A}(S)\le r}\mathcal H_S.
   }
   \]
   Hence the degree-`r` observable class is determined exactly by the interaction supports that can be covered by at most `r` retained channels.

2. **The filtration is simplicial and graded.** Define
   \[
   \Delta_r
   =
   \{S\subseteq[d]:\kappa_{\mathcal A}(S)\le r\}.
   \]
   Each `\Delta_r` is downward closed,
   \[
   \Delta_0\subseteq\Delta_1\subseteq\cdots\subseteq 2^U,
   \]
   and if `P^{(r)}` denotes the orthogonal projector onto `W_r`, then
   \[
   \boxed{
   P^{(r)}-P^{(r-1)}
   \text{ is the orthogonal projector onto }
   \bigoplus_{\kappa_{\mathcal A}(S)=r}\mathcal H_S.
   }
   \]
   Thus every interaction face has an exact first multiplicative degree at which it becomes observable.

3. **AF-036 is the degree-one / unrestricted endpoint pair.**
   \[
   \boxed{
   W_1
   =
   \overline{V_{A_1}+\cdots+V_{A_m}}
   }
   \]
   is precisely the Hilbert join from AF-036, while
   \[
   \boxed{
   W_{\kappa_{\mathcal A}(U)}
   =
   V_U
   =
   L^2\!\left(\bigvee_{j=1}^m\mathcal F_{A_j}\right).
   }
   \]
   If every coordinate in `U` is nontrivial, then `\kappa_{\mathcal A}(U)` is the smallest `r` for which `W_r=V_U`.

4. **Target-relative minimal multiplicative degree is exact.** For
   \[
   g=\sum_{S\subseteq[d]}g_S\in L^2(Q),
   \qquad g_S\in\mathcal H_S,
   \]
   define
   \[
   r_*(g)
   =
   \max\{\kappa_{\mathcal A}(S):g_S\ne0\},
   \]
   with the value `\infty` if some nonzero component has support outside `U`. Then
   \[
   \boxed{
   g\in W_r
   \iff
   r\ge r_*(g).
   }
   \]
   Moreover,
   \[
   \boxed{
   \inf_{w\in W_r}\|g-w\|_2^2
   =
   \sum_{\kappa_{\mathcal A}(S)>r}\|g_S\|_2^2.
   }
   \]
   So the exact approximation defect is the energy carried by interaction faces whose channel-cover complexity exceeds the permitted multiplicative degree.

5. **The full completion cost is a set-cover invariant.** Under coordinate nontriviality,
   \[
   \boxed{
   \min\{r:W_r=V_U\}
   =
   \kappa_{\mathcal A}(U),
   }
   \]
   the minimum number of retained channel sets whose union covers all coordinates visible anywhere upstream. More generally, the minimum multiplicative degree needed for a target family `\mathcal G\subseteq L^2(Q)` is
   \[
   \boxed{
   \max_{g\in\mathcal G}
   \max_{S:g_S\ne0}
   \kappa_{\mathcal A}(S).
   }
   \]

6. **Weighted channel costs give weighted set cover.** If channel `A_j` has positive cost `c_j`, define
   \[
   \kappa_c(S)
   =
   \min\left\{
   \sum_{j\in I}c_j:
   S\subseteq\bigcup_{j\in I}A_j
   \right\}.
   \]
   If the admissible multiplicative monomials are products using a distinct-channel set `I` of total cost at most `B`, their closed span is exactly
   \[
   \boxed{
   \bigoplus_{\kappa_c(S)\le B}\mathcal H_S.
   }
   \]
   Thus minimum-cost multiplicative recovery of an interaction support is literally the corresponding weighted set-cover problem on the channel hypergraph.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{multiplicative recovery is not an undifferentiated nonlinear escape: every interaction has an exact channel-cover degree.}
}
\]

This refines AF-036 from a binary distinction between the linear join and the fully generated algebra/sigma-field to a complete finite filtration measuring exactly how much cross-channel multiplicative structure is required.

## Derivation

### Upper bound: a degree-`r` product cannot escape an `r`-channel union

Take

\[
F=\prod_{\ell=1}^{k}f_\ell,
\qquad
k\le r,
\qquad
f_\ell\in L^\infty(\mathcal F_{A_{j_\ell}}).
\]

The product is bounded and measurable with respect to

\[
\mathcal F_B,
\qquad
B=\bigcup_{\ell=1}^{k}A_{j_\ell}.
\]

Therefore AF-034 gives

\[
F\in V_B
=
\bigoplus_{S\subseteq B}\mathcal H_S.
\]

Every `S\subseteq B` can be covered by the at most `k\le r` channel sets used in the product, hence

\[
\kappa_{\mathcal A}(S)\le r.
\]

Every generator of `W_r` therefore lies in

\[
\bigoplus_{\kappa_{\mathcal A}(S)\le r}\mathcal H_S.
\]

The latter is a finite orthogonal sum of closed subspaces, hence closed, so taking linear spans and `L^2` closure proves

\[
W_r
\subseteq
\bigoplus_{\kappa_{\mathcal A}(S)\le r}\mathcal H_S.
\]

Repeated factors from one channel do not enlarge the bound: their product remains `\mathcal F_{A_j}`-measurable and can be collapsed to a single same-channel factor.

### Lower bound: every covered interaction is synthesized at its cover degree

Now fix `S` with

\[
\kappa_{\mathcal A}(S)=k\le r.
\]

Choose channel indices `j_1,\ldots,j_k` whose union covers `S`. Bounded centered functions are dense in each `L^2_0(q_i)`, so bounded elementary tensors of the form

\[
h_S(x)
=
\prod_{i\in S}\phi_i(x_i),
\qquad
\phi_i\in L^\infty(q_i)\cap L^2_0(q_i),
\]

have dense span in `\mathcal H_S`.

Assign every coordinate `i\in S` to one selected channel `A_{j_\ell}` containing it. For each selected channel put

\[
f_\ell(x)
=
\prod_{\substack{i\in S\\ i\text{ assigned to }j_\ell}}
\phi_i(x_i).
\]

Then `f_\ell\in L^\infty(\mathcal F_{A_{j_\ell}})` and

\[
h_S=\prod_{\ell=1}^{k}f_\ell.
\]

Hence every bounded elementary tensor in `\mathcal H_S` belongs to the algebraic degree-`k` span, and density yields

\[
\mathcal H_S\subseteq W_k\subseteq W_r.
\]

Combining the two inclusions proves the exact filtration.

### Orthogonal grading and approximation defect

Because the Hoeffding spaces are mutually orthogonal and `\Delta_r` is increasing,

\[
W_r\ominus W_{r-1}
=
\bigoplus_{\kappa_{\mathcal A}(S)=r}\mathcal H_S.
\]

The difference of the nested orthogonal projectors `P^{(r)}-P^{(r-1)}` is therefore itself the orthogonal projector onto that grade.

Likewise the best approximation of `g=\sum_Sg_S` in `W_r` is obtained by deleting precisely the components with `\kappa_{\mathcal A}(S)>r`, giving the displayed Pythagorean defect formula.

### Why the completion degree is `\kappa(U)`

Every support `S\subseteq U` obeys

\[
\kappa_{\mathcal A}(S)
\le
\kappa_{\mathcal A}(U),
\]

so the main theorem gives `V_U\subseteq W_{\kappa(U)}`; the reverse inclusion is automatic because all channel products are `\mathcal F_U`-measurable.

If all coordinates are nontrivial, then `\mathcal H_U\ne\{0\}`. For any `r<\kappa_{\mathcal A}(U)`, the whole nonzero interaction space `\mathcal H_U` is absent from `W_r`. Hence no smaller degree can equal `V_U`.

This is sharper than counting channels: redundant or overlapping channels can make `\kappa(U)` much smaller than `m`.

## Minimal controls

### Singleton channels recover ordinary interaction order

If

\[
A_j=\{j\},
\qquad
j=1,\ldots,d,
\]

then

\[
\kappa_{\mathcal A}(S)=|S|.
\]

Therefore

\[
W_r
=
\bigoplus_{|S|\le r}\mathcal H_S.
\]

The familiar hierarchy by interaction order is exactly the special case in which every channel carries one coordinate. AF-032's Boolean low-degree Walsh hierarchy is the finite binary specialization of the same statement.

### Two overlapping channels expose a genuine degree-two gap

Let

\[
A_1=\{1,2\},
\qquad
A_2=\{2,3\}.
\]

Then degree one retains precisely interactions supported entirely inside one of the two channels:

\[
W_1
=
\bigoplus_{S\subseteq\{1,2\}\ \text{or}\ S\subseteq\{2,3\}}
\mathcal H_S.
\]

The supports `\{1,3\}` and `\{1,2,3\}` have channel cover number two. Hence

\[
W_2=V_{\{1,2,3\}},
\]

and the exact degree-two grade is

\[
W_2\ominus W_1
=
\mathcal H_{\{1,3\}}
\oplus
\mathcal H_{\{1,2,3\}}.
\]

Choosing bounded centered nonzero `u(X_1)` and `v(X_3)`, the product `u(X_1)v(X_3)` cannot be synthesized linearly from the two channel spaces but appears as a product of one `A_1`-measurable factor and one `A_2`-measurable factor. This is the smallest nontrivial instance of the cover-degree theorem.

## Destination-category boundary

The theorem concerns **upstream observable functions** that remain available for pointwise multiplication before measurement. It does not say that already-compressed channel outputs can be multiplied to reconstruct missing joint information.

In particular, knowing separate marginal laws, scalar expectations, moments, traces, spectral summaries, or other downstream channel values need not determine the expectation or distribution of a product of upstream observables. AF-030 classifies exact linear-test fidelity by the actually retained closed test span; AF-031 shows that complete separate marginals can forget coupling; AF-036 separates the generated upstream sigma-field from post-compression closure of separate channel values.

Therefore the legitimate pipeline is

\[
\text{upstream channel observables}
\longrightarrow
\text{bounded products of declared channel degree}
\longrightarrow
\text{measurement},
\]

not

\[
\text{separately compressed outputs}
\longrightarrow
\text{invented cross-products}.
\]

The latter arrow requires an independent factorization theorem through the actual destination. Without it, increasing the formal polynomial degree merely reintroduces information that the compression erased.

## Prior art and novelty assessment

No novelty is claimed for Hoeffding/ANOVA decompositions, tensor-product interaction spaces, additive versus multiplicative interaction models, hierarchical/simplicial statistical models, hypergraph set cover, or weighted set cover.

- Akimichi Takemura, **“Tensor Analysis of ANOVA Decomposition,”** *Journal of the American Statistical Association* 78(384), 894–900 (1983), DOI `10.1080/01621459.1983.10477037`. Role: classical tensor/multilinear formulation of ANOVA-type decompositions in `L^2`; anchors the orthogonal interaction spaces used in AF-034 and here.
- J. N. Darroch and T. P. Speed, **“Additive and Multiplicative Models and Interactions,”** *The Annals of Statistics* 11(3), 724–738 (1983), DOI `10.1214/aos/1176346240`. Role: direct classical prior art for organizing additive and multiplicative models through generalized interactions and prescribed marginals; prevents treating multiplication as a new interaction-recovery idea.
- Claude Berge, ***Hypergraphs: Combinatorics of Finite Sets***, North-Holland Mathematical Library 45, North-Holland (1989), ISBN `978-0-444-87489-4`. Role: standard hypergraph/set-family language in which the channel family `\mathcal A` is a hypergraph and `\kappa_{\mathcal A}(S)` is the minimum number of hyperedges needed to cover the target vertex set `S`.
- Mathias Drton, Bernd Sturmfels, and Seth Sullivant, ***Lectures on Algebraic Statistics***, Oberwolfach Seminars 39, Birkhäuser (2009), DOI `10.1007/978-3-7643-8905-5`. Role: authoritative modern background for hierarchical interaction models, conditional independence, and simplicial-complex organization of discrete statistical models.

A targeted prior-art search also found modern binary hierarchical-model work in which arbitrary simplicial complexes index marginal polytopes, reinforcing that the simplicial/hierarchical language itself is mature. The exact theorem above is derived directly by combining AF-034's product Hoeffding decomposition with the elementary hypergraph cover invariant. No claim is made that this packaging is historically novel.

Its Arithmetic Fidelity value is the **resource classification** it supplies: once the admissible nonlinear closure is explicitly bounded by the number or cost of upstream channels allowed to interact, each lost interaction face receives an exact minimum recovery budget. This turns the vague prescription “retain relational information” into a falsifiable statement about which relations become available at which declared multiplicative complexity.

## Boundaries and failure modes

- The exact orthogonal face formula uses the product reference law `Q`. For dependent inputs, AF-035 shows that raw coordinate conditional expectations do not generally realize the Boolean meet calculus; a different dependent-input interaction decomposition must be justified before importing this theorem.
- The factors are taken in `L^\infty` so finite products remain in `L^2`. Products of arbitrary `L^2` functions need not belong to `L^2`.
- `\kappa_{\mathcal A}` counts **channel factors**, not coordinate polynomial degree. One rich channel can already contain arbitrarily high coordinate-order interactions internal to its own set.
- Coordinate nontriviality is needed only for sharp statements that infer the minimal full-completion degree from the nominal top face `U`; the subspace identity itself remains valid when some Hoeffding faces vanish.
- The weighted extension charges distinct channels. Reusing one channel does not buy new coordinate support and can be collapsed into one same-channel bounded factor.
- The theorem classifies the ambient product-space observable class. A particular target discriminator may live at much lower cover degree than full recovery of `V_U`.
- A low cover number is not evidence that the resulting product observable is canonical or physically/mathematically admissible in another destination category. Admissibility of the multiplication itself remains an independent gate.
- Nothing in the theorem makes a rational-prime discriminator survive a spectral, positive, asymptotic, or other later compression. An arithmetic application must still show that the relevant interaction support is prime-specific and that the downstream map retains it.

## Consequence for the line

AF-033 identified coordinate-marginal information states with downward-closed simplicial complexes. AF-034 realized those faces as exact Hoeffding interaction subspaces on product spaces. AF-035 identified mutual independence as the rigidity condition behind the Boolean projection meet law. AF-036 then showed that generated measurable/algebraic joins can fill interactions absent from the linear Hilbert join, but only while upstream observables remain available.

The present result supplies the missing interpolation:

\[
\boxed{
\Delta_r
=
\{S:\kappa_{\mathcal A}(S)\le r\}
}
\]

is the exact information state reachable using at most `r` multiplicatively coupled channels, and

\[
\boxed{
W_r\ominus W_{r-1}
=
\bigoplus_{\kappa_{\mathcal A}(S)=r}\mathcal H_S
}
\]

is its exact newly recovered interaction layer.

The next useful question is therefore no longer whether “nonlinearity” can repair a compression in the abstract. It is whether the **specific nonlinear operations admitted by the destination category** generate a filtration whose grades can be characterized as sharply as this channel-cover model, and whether an intended discriminator enters before the category's admissible complexity ceiling.
