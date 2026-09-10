# MI-012 — Xi source rigidity reaches the single square lattice, but identification is not transition coercivity

**Evidence level:** exact tail/finite-jet controls, Jacobi-reflection and complete-monotonicity counterexamples, plus Hamburger rigidity on the exact square lattice through XF-168

## Core intuition

The Xi source hierarchy now has a sharp boundary. Tail asymptotics, any fixed bank of local source jets, positive real-axis Jacobi-reflecting prekernels, and even complete monotonicity do not determine the heat origin. They can all survive positive mixtures of scaled theta spectra whose `t=0` transform has nonreal zeros.

But once the inverse-Laplace support is fixed to the **single** square lattice `pi n^2`, the apparent coefficient freedom disappears: Jacobi reciprocity and the standard constant term force the ordinary theta weights exactly. This identifies Xi's source representation, yet source identification by itself still does not explain why the distinguished heat slice should lie on the real-rooted side of the transition.

## Strongest justified principle

XF-163--XF-166 show that Gaussian heat translation, beyond-all-orders analytic splicing, arbitrary finite source-jet matching, and positive Green reconstruction of the real-axis Jacobi law all preserve misleading source descriptors while allowing a shifted Xi orbit with nonreal `t=0` zeros.

XF-167 strengthens the control substantially. Averaging translated Xi sources with a positive symmetric measure preserves positivity, the exact Jacobi reflection, cusp normalization, and complete monotonicity. Its inverse-Laplace measure is a positive union of several scaled square lattices, while the Fourier transform acquires explicit nonreal zeros and a positive de Bruijn--Newman threshold. Complete monotonicity therefore does not recover the missing arithmetic support law.

XF-168 fixes the support instead. For `F_a(x)=sum a_n exp(-pi n^2 x)`, absolute Dirichlet convergence plus `Theta_a(x)=x^-1/2 Theta_a(1/x)` produces the completed zeta functional equation and finite-order growth required by Hamburger's converse theorem. Hence the Dirichlet series is `zeta` and every `a_n=1`. No positivity assumption on the weights is needed. The surviving freedom in XF-167 is therefore support contamination, not reweighting of the exact Xi lattice.

## Program consequence

Treat coefficient/support identification and transition coercivity as two separate obligations. The next useful theorem should connect the exact single-square-lattice source law to the collision-forming mesoscopic mass, heat-flow energy, or another quantity that can force the de Bruijn--Newman threshold to be at most zero. Merely deriving another characterization that uniquely identifies Xi is not enough unless it yields such quantitative control.

A secondary route is to derive the single-lattice support law from a cheaper intrinsic source condition that already carries a usable positivity/coercivity consequence; that would combine identification and dynamics rather than append one more identifier.

## Counterevidence / boundary

Hamburger rigidity is a source uniqueness theorem, not RH. The ordinary Xi theta source already satisfies it regardless of whether RH is assumed, so the theorem cannot by itself decide the zero geometry of `H_0`. XF-167 also shows that complete monotonicity is too weak only when multiple scaled lattices are allowed; it does not weaken the exact single-lattice theorem.

More general complex modular structure may encode the same support rigidity in another form, but equivalence to source identification alone would not solve the remaining heat-transition problem.

## Epistemic status

**Exact source boundary: positive Jacobi-reflecting complete-monotone prekernels can still have the wrong heat origin if their Laplace support mixes scaled square lattices, while Jacobi reciprocity on the single Xi square lattice is Hamburger-rigid and forces the exact theta weights. The unresolved step is to convert that identified arithmetic source into transition coercivity.**

## Falsification criterion

Produce nontrivial weights on the fixed support `pi n^2` satisfying the XF-168 convergence, normalization, and Jacobi reciprocity hypotheses, or derive real-rootedness at `t=0` from source identification alone without any additional transition/collision estimate and reconcile that implication with the known equivalence to RH.
